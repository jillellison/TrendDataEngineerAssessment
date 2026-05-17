--This code will create the tables

PRAGMA foreign_keys = ON;

--Create table of Movies

CREATE TABLE IF NOT EXISTS movies (
    tmdb_id             INTEGER PRIMARY KEY,
    imdb_id             TEXT,
    title               TEXT NOT NULL,
    original_title      TEXT,
    original_language   TEXT,
    release_date        TEXT,
    release_year        INTEGER,
    runtime_min         INTEGER,
    status              TEXT,
    vote_average        REAL,
    vote_count          INTEGER,
    popularity          REAL,
    budget_usd          REAL,
    revenue_usd         REAL,
    profit_usd          REAL,
    roi_pct             REAL,
    genres              TEXT,
    us_certification    TEXT,
    production_companies TEXT,
    production_countries TEXT,
    directors           TEXT,
    director_ids        TEXT,
    cast_names          TEXT,
    cast_ids            TEXT,
    collection_name     TEXT,
    tagline             TEXT,
    overview            TEXT
);

CREATE INDEX IF NOT EXISTS idx_movies_release_year ON movies(release_year);
CREATE INDEX IF NOT EXISTS idx_movies_vote_average ON movies(vote_average);
CREATE INDEX IF NOT EXISTS idx_movies_popularity ON movies(popularity);

--Create table of TV shows

CREATE TABLE IF NOT EXISTS tv_shows (
    tmdb_id             INTEGER PRIMARY KEY,
    imdb_id             TEXT,
    title               TEXT NOT NULL,
    original_language   TEXT,
    first_air_date      TEXT,
    last_air_date       TEXT,
    release_year        INTEGER,
    status              TEXT,
    show_type           TEXT,
    number_of_seasons   INTEGER,
    number_of_episodes  INTEGER,
    avg_episode_runtime INTEGER,
    vote_average        REAL,
    vote_count          INTEGER,
    popularity          REAL,
    genres              TEXT,
    networks            TEXT,
    creators            TEXT,
    cast_names          TEXT,
    cast_ids            TEXT,
    origin_countries    TEXT,
    overview            TEXT
);

CREATE INDEX IF NOT EXISTS idx_tv_release_year  ON tv_shows(release_year);
CREATE INDEX IF NOT EXISTS idx_tv_vote_average  ON tv_shows(vote_average);
CREATE INDEX IF NOT EXISTS idx_tv_popularity    ON tv_shows(popularity);

--Create table of actors
CREATE TABLE IF NOT EXISTS people (
    tmdb_id             INTEGER PRIMARY KEY,
    imdb_id             TEXT,
    name                TEXT NOT NULL,
    gender              TEXT,
    birthday            TEXT,
    deathday            TEXT,
    place_of_birth      TEXT,
    known_for_dept      TEXT,
    popularity          REAL,
    total_movie_credits INTEGER,
    total_tv_credits    INTEGER,
    total_directed      INTEGER,
    biography           TEXT
);

CREATE INDEX IF NOT EXISTS idx_people_known_for_dept ON people(known_for_dept);
CREATE INDEX IF NOT EXISTS idx_people_popularity ON people(popularity);

-- Create movie reviews table
CREATE TABLE IF NOT EXISTS movie_reviews (
    review_id   TEXT PRIMARY KEY,
    tmdb_id     INTEGER NOT NULL,
    author      TEXT,
    rating      REAL,
    content     TEXT,
    created_at  TEXT,
    FOREIGN KEY (tmdb_id) REFERENCES movies(tmdb_id)
);

CREATE INDEX IF NOT EXISTS idx_movie_reviews_tmdb_id ON movie_reviews(tmdb_id);
CREATE INDEX IF NOT EXISTS idx_movie_reviews_rating ON movie_reviews(rating);

--Create tv reviews table
CREATE TABLE IF NOT EXISTS tv_reviews(
    review_id           TEXT PRIMARY KEY,
    tmdb_id             INTEGER NOT NULL,
    author              TEXT,
    rating              REAL,
    content             TEXT,
    created_at          TEXT,
    FOREIGN KEY (tmdb_id) REFERENCES tv_shows(tmdb_id)
    );

CREATE INDEX IF NOT EXISTS idx_tv_review_tmdb_id ON tv_reviews(tmdb_id);
CREATE INDEX IF NOT EXISTS idx_tv_reviews_rating ON tv_reviews(rating);
