import pandas as pd

# projekt wymaga biblioteki pandas; instalacja `pip install pandas`
# more: https://pandas.pydata.org/docs/user_guide/10min.html

df = pd.read_csv('data/tmdb_5000_movies.csv')
# print(df.dtypes)
"""
budget                    int64
genres                   object
homepage                 object
id                        int64
keywords                 object
original_language        object
original_title           object
overview                 object
popularity              float64
production_companies     object
production_countries     object
release_date             object
revenue                   int64
runtime                 float64
spoken_languages         object
status                   object
tagline                  object
title                    object
vote_average            float64
vote_count                int64
"""
# print(type(df['title']))  # pandas.core.series.Series

# print(df.index)  # RangeIndex(start=0, stop=4803, step=1)
# print(df.describe())  #średnie, kwantyle etc

# print(df['genres'][0:10])   # 10 rzędów z kolumny 'genres'

df_sub = df.loc[:, ['title', 'homepage', 'tagline']]  # wycinek tabel
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(type(df_sub))  # <class 'pandas.core.frame.DataFrame'>

df_as_dict = df_sub.to_dict(orient='records')
print(type(df_as_dict))  # list
print(type(df_as_dict[0]))  # dict,
print(df_as_dict[0])
# {'title': 'Avatar', 'homepage': 'http://www.avatarmovie.com/', 'tagline': 'Enter the World of Pandora.'}

for movie in df_as_dict:
    print(f"{movie['title']}\t tag:{movie['tagline']}")
