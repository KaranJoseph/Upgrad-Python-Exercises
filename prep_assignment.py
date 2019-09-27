# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:13:16 2019

@author: ASUS
"""
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
movies = pd.read_csv('C:\\Users\\ASUS\Desktop\\Upgrad\\Preparatory Sessions\\Python Data Science\\Assignment\\Movie+Assignment+Data.csv')

# Write your code for dropping the columns here. It is advised to keep inspecting the dataframe after each set of operations 
movies=movies.drop(['color','director_facebook_likes','actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes','actor_2_name','cast_total_facebook_likes','actor_3_name','duration','facenumber_in_poster','content_rating','country','movie_imdb_link','aspect_ratio','plot_keywords',
],axis=1)
movies=movies[~np.isnan(movies['gross'])]
movies=movies[~np.isnan(movies['budget'])]
movies=movies[movies.isnull().sum(axis=1)<=5]
movies.loc[pd.isna(movies['language']), ['language']]='English'
movies[['budget','gross']]=movies[['budget','gross']]/10**6
movies['Profit']=movies['gross']-movies['budget']
movies.drop_duplicates(inplace=True)
movies=movies.sort_values(by='Profit',ascending=False)
top10 = movies.iloc[0:10,:]
IMDb_Top_250=movies[movies.num_voted_users>=25000].sort_values(by='imdb_score',ascending=False).iloc[:250,:]
IMDb_Top_250['Rank']=np.arange(len(IMDb_Top_250))
Top_Foreign_Lang_Film =IMDb_Top_250[IMDb_Top_250.language!='English']
#top10director=movies.groupby('director_name').mean().sort_values(by='imdb_score',ascending=False).iloc[:10,0]
top10director=pd.DataFrame(movies.groupby('director_name')['imdb_score'].mean().sort_values(ascending=False).iloc[:10])
movies['genres']=movies.genres.str.split('|')
movies['genre_1']=movies['genres'].apply(lambda x:x[0])
movies['genre_2']=movies.genres.apply(lambda x:x[1] if len(x)>1 else x[0])
PopGenre=pd.DataFrame(movies.groupby(['genre_1','genre_2'])['gross'].mean().sort_values(ascending=False)).iloc[5:]
Leo_Caprio = movies[movies['actor_1_name']=='Leonardo DiCaprio']
Meryl_Streep = movies[movies['actor_1_name']=='Meryl Streep']
Brad_Pitt = movies[movies['actor_1_name']=='Brad Pitt']
Combined=pd.concat([Meryl_Streep,Leo_Caprio,Brad_Pitt])