"""Lets answer some questions about our tables"""

import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "cinegraph.db")
OUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

#make an output folder
os.makedirs(OUT_DIR, exist_ok=True)

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    return connection

def question1_tv_genres_by_decade():
    print("\n** Question 1:  What are the most popular TV genres by decade? **")
    conn = get_connection()

    df = pd.read_sql_query("""
    SELECT 
        CAST(release_year / 10 AS INTEGER) * 10 AS decade,
        genres,
        popularity
    FROM tv_shows
    WHERE release_year IS NOT NULL
    AND genres IS NOT NULL
    AND popularity IS NOT NULL
    """, conn)
    conn.close()

    df["genres"] = df["genres"].str.split(",")
    df = df.explode("genres")
    df["genres"] = df["genres"].str.strip()

    result = (
        df.groupby(["decade", "genres"])["popularity"].mean().reset_index()
    )
    top_per_decade = (
        result.sort_values(by="popularity", ascending=False).groupby("decade").first().reset_index()
    )
    top_per_decade = top_per_decade.rename(columns={
        "decade": "Decade",
        "genres": "Top Genre",
        "popularity": "Avg Popularity Score"
    })
    top_per_decade["Avg Popularity Score"] = top_per_decade["Avg Popularity Score"].round(1)
    top_per_decade["Decade"] = top_per_decade["Decade"].astype(int).astype(str) + "s"

    print(top_per_decade.to_string(index=False))
    print("\n** NOTE: Popularity scores are weighted metrics based on views,")
    print("  watchlist adds, and voting activity. Higher score equates to more engagement.")


    plt.figure(figsize=(12, 6))
    plt.bar(top_per_decade["Decade"].astype(str), top_per_decade["Avg Popularity Score"], color="steelblue")
    plt.title("Most Popular TV Genre Per Decade")
    plt.xlabel("Decade")
    plt.ylabel("Avg Popularity Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "question1_tv_genres_by_decade.png"))
    plt.close()

def question2_runtime_of_highest_rated_movies():
    print("\n** Question 2:  When looking at the highest rated movies, what is the average runtime? **")
    conn = get_connection()

    df = pd.read_sql_query("""
    SELECT 
        title,
        vote_average,
        vote_count,
        runtime_min
    FROM movies
    WHERE vote_average >= 8.0
    AND vote_count >= 100
    AND runtime_min IS NOT NULL
    ORDER BY vote_average DESC
    """, conn)
    conn.close()

    avg_runtime = df["runtime_min"].mean()
    print(f"  Number of high rated movies (8.0+): {len(df):,}")
    print(f"  Average runtime: {avg_runtime:.1f} minutes")
    print(f"\n Top 10:")

    df = df.rename(columns={
        "title": "Movie Title",
        "vote_average": "Movie Vote Average",
        "vote_count": "Movie Vote Count",
        "runtime_min": "Movie Runtime (min)"
    })
    df["Movie Vote Count"] = df["Movie Vote Count"].fillna(0).astype(int)
    print(df.head(10).to_string(index=False))

    plt.figure(figsize=(10,5))
    plt.hist(df["Movie Runtime (min)"], bins=30, color="coral", edgecolor="black")
    plt.axvline(avg_runtime, color="navy", linestyle="--", label=f"Average: {avg_runtime:1f} minutes")
    plt.title("Runtime of highest rated movies")
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Number of movies")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "question2_runtime_of_highest_rated_movies.png"))
    plt.close()

def question3_popularity_vs_runtime():
    print("\n** Question 3:  Do higher runtimes equal lower popularity? **")
    conn = get_connection()

    df = pd.read_sql_query("""
    SELECT
        title,
        runtime_min,
        popularity
    FROM movies
    WHERE runtime_min IS NOT NULL
    AND popularity IS NOT NULL
    AND runtime_min BETWEEN 60 and 240
    """, conn)
    conn.close()

    correlation = df["runtime_min"].corr(df["popularity"])
    print(f" Number of movies analyzed: {len(df):,}")
    print(f" Relationship between runtime and popularity: {correlation:.2f}")
    print(" (Scale: -1.0 = negative, 0 = none, 1.0 = positive)")

    plt.figure(figsize=(10,6))
    plt.scatter(df["runtime_min"], df["popularity"], label="Popularity")
    plt.title("Popularity vs Runtime")
    plt.xlabel("Runtime in minutes")
    plt.ylabel("Popularity")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "question3_popularity_vs_runtime.png"))
    plt.close()
    print("\n ** NOTE: If you open the chart saved in our outputs folder you can see the plots"
          "\n to get a clear story of whether there is a relationship between runtime and popularity. **")

def question4_busiest_actors_and_genres():
    print("\n** Question 4: What genres do the top people tend to work in? **"
          "\n --Please be patient.  This is a lot of data--")
    conn = get_connection()

    df = pd.read_sql_query("""
    SELECT 
        p.name,
        p.known_for_dept,
        p.total_movie_credits,
        p.total_tv_credits,
        m.genres
    FROM people p
    JOIN movies m ON (',' || m.cast_ids || ',') LIKE ('%,' || p.tmdb_id || ',%') 
    WHERE p.total_movie_credits >=20
    AND m.genres IS NOT NULL
    LIMIT 2500
    """, conn)
    conn.close()

    df["genres"] = df["genres"].str.split(",")
    df = df.explode("genres")
    df["genres"] = df["genres"].str.strip()

    df["total_credits"] = df["total_movie_credits"] + df["total_tv_credits"]

    top_genre = (
        df.groupby(["name", "known_for_dept", "total_credits"])["genres"]
        .agg(lambda x: x.value_counts().index[0])
        .reset_index()
        .rename(columns={"genres": "Top Genre"  })
    )

    top_people = top_genre.sort_values("total_credits", ascending=False).head(15)
    top_people = top_people.rename(columns={
        "name": "Name",
        "known_for_dept": "Department",
        "total_credits": "Total Credits"
    })

    print(top_people.to_string(index=False))

def question5_top_25_rated_movies():
    print("\n** Question 5: What are the top 25 highest rated movies? **")
    conn = get_connection()

    df = pd.read_sql_query("""
    SELECT 
        m.title AS Title,
        m.vote_average AS "Avg TMDB Rating",
        COUNT(r.review_id) AS "Review Count",
        ROUND(AVG(r.rating),2) AS "Average Reviewer Rating",
        m.release_year AS "Release Year"
    FROM movies m
    JOIN movie_reviews r ON m.tmdb_id = r.tmdb_id
    WHERE r.rating IS NOT NULL
    GROUP BY m.tmdb_id, m.title, m.vote_average, m.release_year
    HAVING COUNT(r.review_id) >= 10
    ORDER BY m.vote_average DESC
    LIMIT 25""", conn)
    conn.close()
    df["Release Year"] = df["Release Year"].fillna(0).astype(int)
    print(df.to_string(index=False))

def main():
    """Run all Questions"""
    question1_tv_genres_by_decade()
    question2_runtime_of_highest_rated_movies()
    question3_popularity_vs_runtime()
    question4_busiest_actors_and_genres()
    question5_top_25_rated_movies()

if __name__ == "__main__":
    main()