#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("fp_og_csv/Untitled.csv", sep=",")


# In[10]:


print(df)

df.head(5)


# In[11]:


df.describe()


# In[12]:


#df.sort_values('2015-16.4')


# In[13]:


df.tail(5)


# In[ ]:


df.drop(columns=['2015-16.1'])


# In[ ]:


#df = df[['team_name','w_pct','w','l']]


# In[ ]:


#print(df)


# In[ ]:


for index, row in df.iterrows():
    print(index,row['team_name_2016'])


# In[ ]:


df.loc[df['team_name_2015'] == 'Brooklyn Nets']


# In[ ]:


df = df.drop(columns=['gp', 'gp.1', 'gp.2', 'gp.3'] axis=1)


# In[ ]:


print(df)


# In[14]:


df.isnull().sum()


# In[ ]:


df.shape


# In[15]:


#cleaning my data, getting rid of multiple NaN 
df.dropna(inplace = True)

print(df.to_string()) 


# In[ ]:


df.shape


# In[ ]:


df.tail()


# In[ ]:





# In[16]:


df.head(2)


# In[17]:


#first comp.

plt.figure(figsize=(15,15))

plt.plot(df.w_pct_2015, df.team_name_2015, label="2015-16", color="#216331", marker="o")
plt.plot( df.w_pct_2016, df.team_name_2016, label="2016-17", color="#008b91", marker="o")
plt.plot(df.w_pct_2017, df.team_name_2017, label="2017-18", color="#45a8e4", marker="o")
plt.plot(df.w_pct_2018, df.team_name_2018, label="2018-19", color="#dcb8ff",marker="o")


plt.title("2015-2019 Eastern Conference Win %")
plt.xlabel("win %")
plt.legend()

plt.xticks(rotation=17)



plt.show()


# In[8]:


df.groupby('team_name_2016')['w_pct_2016'].mean()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




