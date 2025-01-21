# Project 3: Bauer, Jung and Linder

# Project Overview
This project follows the 'Data Engineering' tract. Its purpose is to make build and populate a working database, using ETL workflows.
A prototype API was also build using Flask, to show how the data could be accessed by users for analysis.

# Sources
Original data source: https://www.kaggle.com/datasets/avenn98/world-of-warcraft-demographics


# Instructions for Use
1. Clone this repo for full use. Additional tools required: PostgreSQL and pgAdmin4.
2. Raw data, that mirrors what is available at the above URL (original source), can be found at /resources/raw.csv
3. Cleaned 'player.csv' and 'character.csv' are both located in the resource folder. To recreate these file, run `csv_transform.py`.
4. Using pgAdmin4, initialize a new database named 'warcraft_df'.
5. Create two new tables using `schema.sql`.
6. Import player.csv and character.csv into their respectively named tables.
7. Install [psycoph2](https://pypi.org/project/psycopg2/), using either `pip install psycopg2` or `conda install psycopg2`.







# Ethical Considerations
The original source of the data is linked above, to ensure that proper visibility is provided to the original source. Additionally, consideration was given to the personal nature of the subject data. Given the use of demographic information, it is important to ensure that the underlying data is anonymous in nature, and cannot be linked individuals.

