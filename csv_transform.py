import pandas
from pathlib import Path

#read in raw data, dump into dataframe
path = Path("resources/raw.csv")
raw_df = pandas.read_csv(path, encoding="utf-8")

#create new dataframes with targeted player demographics and character demographics
player_df = raw_df[["Age", "Gender", "Sexuality", "Country", "Server"]]
character_df = raw_df[["Faction","Main","Role","Class","Race","Type"]]

#adding ID column to player and character DataFrames
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html
player_df = player_df.assign(id=lambda x: [x for x in range(1,len(player_df)+1)])
character_df = character_df.assign(id=lambda x: [x for x in range(1,len(player_df)+1)])

#converting all string values in dataframe to lowercase
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map
#https://www.w3schools.com/python/ref_func_isinstance.asp
player_df = player_df.map(lambda x: x.lower() if isinstance(x, str) else x)
character_df = character_df.map(lambda x: x.lower() if isinstance(x, str) else x)

#reorder columns
player_df = player_df[["id", "Age", "Gender", "Sexuality", "Country", "Server"]]
character_df = character_df[["id","Faction","Main","Role","Class","Race","Type"]]

#change headers to lowercase
player_df = player_df.rename(columns = {"Age":"age", "Gender":"gender", "Sexuality":"sexuality", "Country":"country", "Server": "server"})
character_df = character_df.rename(columns = {"Faction":"faction", "Main":"main", "Role":"role", "Class":"class", "Race": "race","Type":"type"})


player_df.to_csv("resources/players.csv", encoding="utf-8", index=False, header=True)
character_df.to_csv("resources/characters.csv", encoding="utf-8", index=False, header=True)



