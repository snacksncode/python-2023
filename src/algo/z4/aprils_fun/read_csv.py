
import pandas as pd


# projekt wymaga biblioteki pandas; instalacja `pip install pandas`


df = pd.read_csv('data/tmdb_5000_movies.csv')
print(df['title'])

titles = list(df['title'])
# print(titles)

print(df.head())