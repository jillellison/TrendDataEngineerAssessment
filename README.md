#Trend Data Engineer Assessment 
A pipeline built with Python and SQL using
[CineGraph TMDB Movies, TV & People Dataset](https://www.kaggle.com/datasets/muhammetyorulmaz1/cinegraph-tmdb-movies-tv-and-people-dataset) from Kaggle.

##Why I picked this
I chose this dataset because my late husband was a huge movie buff. There wasn't 
a movie or show he hadn't seen. Working with this data felt like a way to stay connected to 
something we both loved - tv and data. Beyond the personal connection, movies and TV shows make 
for a great project. There are multiple naturally related entities 
(movies, shows, people, and reviews), tons of real data, and actual 
interesting questions to ask. Also it wasn't a bad excuse to also find my next movie to watch.


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
├─ main.py             * Run this to execute the whole project
├─ schema.sql          * SQL database schema
├─ er_diagram.png      * Entity relationship diagram
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

##Running the whole project
```bash
python scripts/main.py
```
Results will print and charts save in the outputs folder.

##Questions asked
Question 1:  What are the most popular TV genres by decade?
I was curious if over time, people change their interests.  I know my grandpa was big into westerns but wasn't sure if it was a generational thing or him.
Question 2:  When looking at the highest rated movies, what is the average runtime?
I was curious is a certain average runtime makes a movie more highly rated.  Is there a sweet spot?
Question 3:  Do higher runtimes equal lower popularity? 
Everyone complains when a movie is too long (Wicked) but does it change the ratings?
Question 4: What genres do the top people tend to work in?
Do Hollywood's elite work in similar genres or does that not matter?
Question 5: What are the top 25 highest rated movies? 
Honestly just curiosity - wanted to know if I'd seen them.  You see on facebook people putting add a point for each one you've seen or things like that so this was a sort of exercise like that. Spoiler I only got 6 points.
Question 6: Do TV reviewer ratings match vote averages?
Had to know if people watching agreed with the professionals - they didn't :)
