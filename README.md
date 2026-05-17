#Trend Data Engineer Assessment 
A pipeline built with Python and SQL using
[CineGraph TMDB Movies, TV & People Dataset](https://www.kaggle.com/datasets/muhammetyorulmaz1/cinegraph-tmdb-movies-tv-and-people-dataset) from Kaggle.

##Dataset
movies.csv	22,393 
tv_shows.csv	15,562
people.csv	58,393
orphan_movies.csv	8,068
orphan_tv.csv	3,389
movie_reviews.csv	22,712
tv_reviews.csv	2,923

##Here's how I've organized the project
DataEngineerProject/
├─ data/               * Downloaded CSVs
├─ outputs/            * Generated charts
├─ scripts/
│   ├─ ingest.py       * Downloads and loads data into SQL
│   └─ analysis.py     * Answers 6 questions
├─ schema.sql          * SQL database schema
├─ requirements.txt    * Python dependencies
└─ README.md           * You are here

##What now?
Sign up for a free Kaggle account if you don't already have one to download the dataset.
kaggle.com

##Clone the repo
```bash
git clone <your-repo-url>
cd DataEngineerProject
```

##Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

##Install dependencies
```bash
pip install -r requirements.txt
```

##Set up Kaggle credentials
Either create `~/.kaggle/kaggle.json`:
```json
{"username":"your_kaggle_username","key":"your_kaggle_key"}
```
Or set environment variables:
```bash
export KAGGLE_USERNAME="your_username"
export KAGGLE_KEY="your_key"
```

##Downloading the data and building database
```bash
python scripts/ingest.py
```

##Run analysis.py
```bash
python scripts/analysis.py
```
Results will print and charts save in the outputs folder.

Question 1:  What are the most popular TV genres by decade?
Question 2:  When looking at the highest rated movies, what is the average runtime?
Question 3:  Do higher runtimes equal lower popularity? 
Question 4: What genres do the top people tend to work in?
Question 5: What are the top 25 highest rated movies? 
Question 6: Do TV reviewer ratings match vote averages?