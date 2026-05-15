--This code will create the tables

PRAGMA foreign_keys = ON;

--Create table of Movies

CREATE TABLE movies (
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

CREATE INDEX idx_movies_release_year ON movies(release_year);
CREATE INDEX idx_movies_vote_average ON movies(vote_average);
CREATE INDEX idx_movies_popularity ON movies(popularity);

--Create table of TV shows

CREATE TABLE tv_shows (
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

CREATE INDEX idx_tv_release_year  ON tv_shows(release_year);
CREATE INDEX idx_tv_vote_average  ON tv_shows(vote_average);
CREATE INDEX idx_tv_popularity    ON tv_shows(popularity);

--Create table of actors
CREATE TABLE people (
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

CREATE INDEX idx_people_known_for_dept ON people(known_for_dept);
CREATE INDEX idx_people_popularity ON people(popularity);

--Create reviews table
CREATE TABLE tv_reviews(
    review_id           TEXT PRIMARY KEY,
    tmdb_id             INTEGER NOT NULL,
    author              TEXT,
    rating              REAL,
    content             TEXT,
    created_at          TEXT,
    FOREIGN_KEY (tmbd_id) REFERENCES tv_shows(tmbd_id)
    );

CREATE INDEX idx_tv_review_tmdb_id ON tv_reviews(tmbd_id);
CREATE INDEX idx_tv_reviews_rating ON tv_reviews(rating);
