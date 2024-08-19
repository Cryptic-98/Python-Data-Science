import pandas as pd
# read csv file
df = pd.read_csv('C:\\Users\\Goabaone\\repos\\Python-Data-Science\\pythonProject1\\nba.csv')
# prints the first 5 rows ↓
print(df.head())
# # prints the last 5 rows ↓
print(df.tail())
# shows how many rows and columns the dataset has ↓
print(df.shape)
# prints the first 2 rows ↓
print(df.head(2))
# prints 2 columns (name and team) ↓
print(df[['Name', 'Team']])
