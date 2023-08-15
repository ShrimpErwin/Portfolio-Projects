#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


df = pd.read_csv(r"C:\Users\amitm\Downloads\pandas tutorial\Ice Cream Ratings.csv")
df = df.set_index('Date')
df


# In[27]:


print(plt.style.available)
plt.style.use('fivethirtyeight')


# In[11]:


df.plot(kind ='line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[14]:


df.plot(kind ='bar', stacked = True, xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[16]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, c = 'Blue')


# In[17]:


df.plot.hist(bins = 10)


# In[18]:


df.boxplot()


# In[22]:


df.plot.area(figsize = (10,5))


# In[20]:


df.plot.pie(y='Flavor Rating',figsize=(10,10))


# In[ ]:




