#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import ssl
import certifi
get_ipython().run_line_magic('matplotlib', 'inline')
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv("teamstats2019-20.csv", sep=",")


# In[16]:


df[df['gp']>72].groupby(['team_name', 'w']).mean()


# In[ ]:




df.head()


# In[4]:


df.tail()


# In[5]:


df.sample()


# In[6]:

#check null values

df.isnull().sum()


# In[7]:


pd.unique(df['gp'])


# In[17]:


df2 = df.iloc[[0,1, 2, 3, 4, 5, 8, 11, 15, 16, 19, 21, 22, 27, 29], df.columns.get_indexer(['team_name','l','gp', 'w'])]
df2


# In[ ]:





# In[18]:


sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))


sns.set_color_codes("pastel")
sns.barplot(x="gp", y="team_name", data=df2,
            label="Total Games Played", color="#dcb8ff")

sns.set_color_codes("muted")
sns.barplot(x="w", y="team_name", data=df2,
            label="Games Won", color="#216331")

sns.set_color_codes("muted")
sns.barplot(x="l", y="team_name", data=df2,
            label="Games Lost", color="#45a8e4", alpha=.9)

ax.legend(ncol=3, loc="lower right", frameon=True)
ax.set(xlim=(0, 81), ylabel="",
       xlabel="", title="Eastern Conf. 2019-2020")
sns.despine(left=True, bottom=True)

plt.savefig("bubble.png", bbox_inches="tight")


# In[ ]:





# In[175]:


#raptors or bucks

df_2015 = df.iloc[[ 16, 27], df.columns.get_indexer(['team_name','l','gp', 'w'])]
df_2015



# In[147]:


sns.set_theme(style="whitegrid")
sns.color_palette("husl")
g = sns.catplot(
    data=df3, kind="bar",
    x="team_name", y="gp", hue="w",
    ci="sd", palette="husl", alpha=.9, height=4
)
g.despine(left=True)
g.set_axis_labels("", "games played")
g.legend.set_title("Games Won")

plt.savefig("bubble2.png", bbox_inches="tight")


# In[157]:


df2['w'].mean()


# In[158]:


df2['w'].sum()


# In[159]:


df2['w'].max()


# In[160]:


df2['w'].min()


# In[161]:


df2['w'].count()


# In[162]:


df2['w'].median() 


# In[163]:


df2['w'].std() 


# In[164]:


df2['w'].var()


# In[165]:


pd.unique(df2['gp'])


# In[168]:


#pd.unique(df2['w']), array([48, 35, 23, 22, 19, 20, 45, 44, 56, 21, 33, 43, 53, 25])
#pd.unique(df2['l']), array([24, 37, 42, 43, 46, 28, 29, 17, 45, 40, 30, 19, 47])


# In[169]:


df2['l'].mean()


# In[170]:


df2['l'].std() 


# In[ ]:


#is there a relationship btwn 
#3pm/szn & games won?

