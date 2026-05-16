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
    print("\n --- Question 1:  What are the most popular TV genres by decade?")
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
    print("\n  Note: Popularity scores are weighted metric based on views,")
    print("  watchlist adds, and voting activity. Higher score equates to more engagement.")


    plt.figure(figsize=(12, 6))
    plt.bar(top_per_decade["Decade"].astype(str), top_per_decade["Avg Popularity Score"], color="steelblue")
    plt.title("Most Popular TV Genre Per Decade")
    plt.xlabel("Decade")
    plt.ylabel("Avg Popularity Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "q1_tv_genres_by_decade.png"))
    plt.close()
    print("  Chart saved to outputs/q1_tv_genres_by_decade.png")

def main():
    """Run all Questions"""
    question1_tv_genres_by_decade()

if __name__ == "__main__":
    main()