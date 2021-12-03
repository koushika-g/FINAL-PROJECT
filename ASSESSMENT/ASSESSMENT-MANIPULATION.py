#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


#1st question
movies=pd.read_csv(r"C:\Users\Merit\Desktop\PROJECT\movies.csv",encoding='latin-1')
ratings=pd.read_csv(r"C:\Users\Merit\Desktop\PROJECT\ratings.csv",encoding='latin-1')
data = pd.merge(left=movies, right=ratings, on='movieId')


# In[5]:


data


# In[6]:


ratings.isnull().any()


# In[7]:


ratings['rating'].value_counts()


# In[8]:


#movies that are rated:

Are_rated = data.rating !=0
a=data[Are_rated]

a[['title','rating']]


# In[9]:


###2nd question


# In[13]:


# ratings=pd.read_csv(r"C:\Users\Merit\Desktop\PROJECT\ratings.csv",encoding='latin-1')
# tags=pd.read_csv(r"C:\Users\Merit\Desktop\PROJECT\tags.csv",encoding='latin-1')
# data1 = pd.merge(left=ratings, right=tags ,on='userId')
# data1


# In[12]:


#users that have rated AND tagged a movie:

users = ratings[ratings["userId"].isin(tags["userId"])]
pd.set_option('display.max_rows',None)
uni = users["userId"].unique()
uni


# In[9]:


#3rd question


# In[10]:


#min
min_ratings_per_movie = data.groupby(by = ["movieId", "title"], as_index=False)["rating"].min()
min_ratings_per_movie


# In[11]:


#max
max_ratings_per_movie = data.groupby(by = ["movieId", "title"], as_index=False)["rating"].max()
max_ratings_per_movie


# In[8]:


#average
avg_ratings_per_movie = data.groupby(by = ["movieId", "title"], as_index=False)["rating"].mean()
avg_ratings_per_movie


# In[12]:


#4th question


# In[26]:


average_rating=data.groupby(["movieId","title"], as_index=False)["rating"].mean()
average_rating


# In[27]:


rating_count=data.groupby(["movieId","title"], as_index=False)["rating"].count()
rating_count


# In[29]:


ques = pd.merge(left=rating_count, right=average_rating, on='movieId')
ques


# In[30]:


n=ques.drop(columns='title_y')


# In[31]:


#appends a rating count and average rating for each movie:

add_column = n.rename(columns = {'title_x':'title','rating_x': 'rating_count', 'rating_y': 'average_rating'}, inplace = False)
add_column


# In[ ]:


#5th question


# In[14]:


from matplotlib import pyplot as plt


# In[16]:


split_genre=(movies["genres"].str.split("|", expand=True).stack())
df = pd.DataFrame(split_genre)
df


# In[17]:


split_movie = movies["title"].str.rsplit(" ", n = 1, expand=True)
movies["Movie Title"] = split_movie[0]
movies["Movie Year"] = split_movie[1]
split_movie


# In[21]:


df.plot.bar()


# In[ ]:




