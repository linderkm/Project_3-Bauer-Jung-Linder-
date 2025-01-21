# Project 3: Bauer, Jung and Linder

# Project Overview
This project follows the 'Data Engineering' tract. Its purpose is to make build and populate a working database, using ETL workflows.
A prototype API was also build using Flask, to show how the data could be accessed by users for analysis.


# Instructions for Use
1. Clone this repo for full use. Additional tools required: PostgreSQL and pgAdmin4.
2. Raw data, that mirrors what is available at the above URL (original source), can be found at /resources/raw.csv
3. Cleaned 'player.csv' and 'character.csv' are both located in the resource folder. To recreate these file, run `csv_transform.py`.
4. Using pgAdmin4, initialize a new database named 'warcraft_df'.
5. Create two new tables using `schema.sql`.
6. Import player.csv and character.csv into their respectively named tables.
7. Install [psycopg2](https://pypi.org/project/psycopg2/), using either `pip install psycopg2` or `conda install psycopg2`.
8. Create a local python file named 'pg_cred.py'. This file will contain the necessary credential details to connect to 'warcraft_db' using psycopg2.
9. In 'pg_cred.py', set `database = 'warcraft_db'`, `user = '<your_username>'`, `host = 'localhost'`, `password = '<your_password>'`, `port = 5432`.
9. To Initialize Flask API, run `app.py`.



# Ethical Considerations
The original source of the data is linked above, to ensure that proper visibility is provided to the original source. Additionally, consideration was given to the personal nature of the subject data. Given the use of demographic information, it is important to ensure that the underlying data is anonymous in nature, and cannot be linked individuals.

# Sources
- Original data source: https://www.kaggle.com/datasets/avenn98/world-of-warcraft-demographics
- DBD Tool: https://www.quickdatabasediagrams.com/
- Psycopg2 library: https://pypi.org/project/psycopg2/