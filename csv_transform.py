import pandas
from pathlib import Path

#read in raw data, dump into dataframe
path = Path("resources/raw.csv")
raw_df = pandas.read_csv(path, encoding="utf-8")

#create new dataframe with targeted player demographics
player_df = raw_df[["Age", "Gender", "Sexuality", "Country", "Server"]]

#adding ID column to player data
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html
player_df = player_df.assign(id=lambda x: [x for x in range(1,len(player_df)+1)])

#converting all string values in dataframe to lowercase
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map
#https://www.w3schools.com/python/ref_func_isinstance.asp
player_df = player_df.map(lambda x: x.lower() if isinstance(x, str) else x)

#reorder columns
player_df = player_df[["id", "Age", "Gender", "Sexuality", "Country", "Server"]]

player_df = player_df.rename(columns = {"Age":"age", "Gender":"gender", "Sexuality":"sexuality", "Country":"country", "Server": "server"})



print(player_df.head())



