import os
import sqlite3
import subprocess
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR    = os.path.join(BASE_DIR, "data", "cinegraph-2026")
DB_PATH     = os.path.join(BASE_DIR, "cinegraph.db")
DATASET     = "muhammetyorulmaz1/cinegraph-tmdb-movies-tv-and-people-dataset"

def download_data():
    """Downloading data if not there yet."""
    if os.path.exists(DATA_DIR):
        print("You already have the data downloaded.  We're gonna skip to the next step.  You're too good!")
        return
    print("We are now downloading the dataset.  I know you're excited!")
    env = os.environ.copy()
    env["KAGGLE_USERNAME"] = os.environ.get("KAGGLE_USERNAME", "")
    env["KAGGLE_KEY"] = os.environ.get("KAGGLE_KEY", "")
    download_path = os.path.join(BASE_DIR, "data")
    subprocess.run([
        "kaggle", "datasets", "download",
        DATASET,
        "--unzip",
        "-p", download_path
    ], check=True, env=env)
    print("You got this! Download completed.")

def create_database():
        """Create the tables here from the schema file"""
        schema_path = os.path.join(BASE_DIR, "schema.sql")
        print ("Now creating our tables. Here we go...")
        with sqlite3.connect(DB_PATH) as conn:
            with open(schema_path, "r") as f:
                conn.executescript(f.read())
        print("All done.  It was worth the wait")

def load_movies(conn):
        """Loading the movies table"""
        print("Here come the movies.")
        df = pd.read_csv(os.path.join(DATA_DIR, "movies.csv"), low_memory=False)

        #listing the columns I want to keep
        columns = [
            "tmdb_id", "imdb_id", "title", "original_title", "original_language",
            "release_date", "release_year", "runtime_min", "status", "vote_average",
            "vote_count", "popularity", "budget_usd", "revenue_usd", "profit_usd",
            "roi_pct", "genres", "us_certification", "production_companies",
            "production_countries", "directors", "director_ids", "cast_names",
            "cast_ids", "collection_name", "tagline", "overview"
        ]
        df = df[columns]
        df.to_sql("movies", conn, if_exists="replace", index=False)
        print(f"  Loaded {len(df)} movies.")

def load_tv_shows(conn):
    """Loading TV shows"""
    print("And now...TV SHOWS!")
    df = pd.read_csv(os.path.join(DATA_DIR, "tv_shows.csv"), low_memory=False)

    # list of columns again
    columns = [
        "tmdb_id", "imdb_id", "title", "original_language", "first_air_date",
        "last_air_date", "release_year", "status", "show_type",
        "number_of_seasons", "number_of_episodes", "avg_episode_runtime",
        "vote_average", "vote_count", "popularity", "genres", "networks",
        "creators", "cast_names", "cast_ids", "origin_countries", "overview"
    ]
    df = df[columns]

    df.to_sql("tv_shows", conn, if_exists="replace", index=False)
    print(f"  Loaded {len(df):,} TV shows.")

def load_people(conn):
    """Loading actors"""
    print("Of course we need all the actors as well! Here they come!")
    df = pd.read_csv(os.path.join(DATA_DIR, "people.csv"), low_memory=False)

    # Columns list
    columns = [
        "tmdb_id", "imdb_id", "name", "gender", "birthday", "deathday",
        "place_of_birth", "known_for_dept", "popularity", "total_movie_credits",
        "total_tv_credits", "total_directed", "biography"
    ]
    df = df[columns]

    df.to_sql("people", conn, if_exists="replace", index=False)
    print(f"  Loaded {len(df):,} people.")

def load_movie_reviews(conn):
    """Loading movie reviews"""
    print("Are they any good? Loading movie reviews.")
    df = pd.read_csv(os.path.join(DATA_DIR, "movie_reviews.csv"), low_memory=False)

    #Columns list
    columns = ["review_id", "tmdb_id", "author", "rating", "content", "created_at"]
    df = df[columns]

    df.to_sql("movie_reviews", conn, if_exists="replace", index=False)
    print(f"  Loaded {len(df):,} movie reviews.")


def load_tv_reviews(conn):
    """Loading tv show reviews"""
    print("Well we gotta know if the tv shows are good too!")
    df = pd.read_csv(os.path.join(DATA_DIR, "tv_reviews.csv"), low_memory=False)

    #Columns list
    columns = ["review_id", "tmdb_id", "author", "rating", "content", "created_at"]
    df = df[columns]

    df.to_sql("tv_reviews", conn, if_exists="replace", index=False)
    print(f"  Loaded {len(df):,} TV reviews.")

def main():
    """Run it all"""
    download_data()
    create_database()

    with sqlite3.connect (DB_PATH) as conn:
        load_movies(conn)
        load_tv_shows(conn)
        load_people(conn)
        load_movie_reviews(conn)
        load_tv_reviews(conn)
    print("That's it! All done and ready at:", DB_PATH)

if __name__ == "__main__":
    main()