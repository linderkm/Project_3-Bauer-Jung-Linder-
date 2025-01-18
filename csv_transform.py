import pandas
from pathlib import Path

#read in raw data, dump into dataframe
path = Path("resources/raw.csv")
raw_df = pandas.read_csv(path, encoding="utf-8")

player_header_reference = ["Gender", "Sexuality", "Age", "Country", "Server"]

#create new dataframe with targeted player demographics
player_df = raw_df[player_header_reference]

#adding ID column to player data
player_df = player_df.assign(id=lambda x: [x for x in range(1,len(player_df)+1)])


print(player_df.head())



