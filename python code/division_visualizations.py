#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
df = pd.read_csv("fp_og_csv/Untitled.csv", sep=",")


# In[7]:


print(df)

df.head(5)


# In[8]:


for index, row in df.iterrows():
    print(index,row['team_name_2016'])


# In[105]:


df.loc[df['team_name_2015'] == 'Brooklyn Nets']


# In[16]:


#df_new = df.drop(columns=['gp', 'gp.1', 'gp.2', 'gp.3'])
print(df)


# In[9]:


df.shape

df.dropna(inplace = True)

print(df.to_string()) 


# In[107]:


df.isnull().sum()


# In[10]:


df.tail()


# # VISUALIZATION ONE - ALL TEAMS, ALL YEARS

# In[11]:


plt.figure(figsize=(15,15))

plt.plot(df.w_pct_2015, df.team_name_2015, label="2015-16", color="#216331", marker="o")
plt.plot( df.w_pct_2016, df.team_name_2016, label="2016-17", color="#008b91", marker="o")
plt.plot(df.w_pct_2017, df.team_name_2017, label="2017-18", color="#45a8e4", marker="o")
plt.plot(df.w_pct_2018, df.team_name_2018, label="2018-19", color="#dcb8ff",marker="o")


plt.title("2015-2019 Eastern Conference Win %")
plt.xlabel("win %")
plt.legend()

plt.xticks(rotation=0)



plt.show()


# # 2015-16 Underdogs

# In[12]:


atlantic_div = ['Boston Celtics', 'Brooklyn Nets', 'Philadelphia 76ers', 'New York Knicks', 'Toronto Raptors']
atlantic_div_df = df.loc[df['team_name_2015'].isin(atlantic_div) ]
atlantic_div_df.to_csv('atlantic_div_df.csv')

plt.rcParams["font.family"] = "Helvetica"

colors = ['#216331','#216331','#216331', '#dcb8ff','#216331',]

X = atlantic_div_df['team_name_2015']
Y = list(atlantic_div_df['w_pct_2015'])

plt.bar(X, Y, width=0.5,  color=colors)
plt.title("2015-16 Season Underdogs - Atlantic Division", fontweight='bold', color = 'black', fontsize='20')
plt.xlabel("Team Name", color = 'blue', fontsize='18')
plt.ylabel("Win %", color = 'blue', fontsize='18')

plt.xticks(X, rotation=15)


plt.show()

#plt2

central_div = ['Cleveland Cavaliers','Milwaukee Bucks','Chicago Bulls', 'Detroit Pistons', 'Indiana Pacers']
central_div_df = df.loc[df['team_name_2015'].isin(central_div) ]
central_div_df.to_csv('central_div_df.csv')

plt.rcParams["font.family"] = "Helvetica"

colors = ['#216331','#216331','#216331', '#216331','#dcb8ff']

X1 = central_div_df['team_name_2015']
Y1 = list(central_div_df['w_pct_2015'])

plt.bar(X1, Y1, width=0.5,  color=colors)
plt.title("2015-16 Season Underdogs - Central Division", fontweight='bold', color = 'black', fontsize='20')
plt.xlabel("Team Name", color = 'blue', fontsize='18')
plt.ylabel("Win %", color = 'blue', fontsize='18')

plt.xticks(X1, rotation=10)


plt.show()

#plt3

se_div = ['Atlanta Hawks','Charlotte Hornets','Miami Heat','Orlando Magic','Washington Wizards']
se_div_df = df.loc[df['team_name_2015'].isin(se_div) ]
se_div_df.to_csv('se_div_df.csv')

plt.rcParams["font.family"] = "Helvetica"

colors = ['#216331','#216331','#216331', '#dcb8ff','#216331']

X2 = se_div_df['team_name_2015']
Y2 = list(se_div_df['w_pct_2015'])

plt.bar(X2, Y2, width=0.5,  color=colors)
plt.title("2015-16 Season Underdogs - SE Division", fontweight='bold', color = 'black', fontsize='20')
plt.xlabel("Team Name", color = 'blue', fontsize='18')
plt.ylabel("Win %", color = 'blue', fontsize='18')

plt.xticks(X2, rotation=10)


plt.show()



# In[115]:


df.tail(10)


# In[116]:


#checking for mistake i made earlier

select_name = df.loc[df['team_name_2017'] == 'Utah Jazz']
print (select_name)


# In[13]:


# only the ny teams over the years
select_nets = df.loc[(df['team_name_2015'] == 'Brooklyn Nets') & (df['team_name_2016'] == 'Brooklyn Nets') & (df['team_name_2017'] == 'Brooklyn Nets') & (df['team_name_2018'] == 'Brooklyn Nets')]
print (select_nets)


select_knicks = df.loc[(df['team_name_2015'] == 'New York Knicks') & (df['team_name_2016'] == 'New York Knicks') & (df['team_name_2017'] == 'New York Knicks') & (df['team_name_2018'] == 'New York Knicks')]
print (select_knicks)


# In[162]:


#new dataframe for just ny teams

#nyc = ['Boston Celtics', 'Brooklyn Nets']
#nyc_df = df.loc[df['team_name-2015'].isin(nyc) ]
#nyc_df.to_csv('nyc.csv')

#new_df = pd.read_csv("nyc.csv", sep=",")
#print(new_df)


# In[25]:


#this is me trying to figure out how to graph only nyc data

#col_names = ['team_name_2015', 'team_name_2016', 'team_name_2017', 'team_name_2018']
#select multiple columns of dataframe by names in list
#multiple_columns = df[col_names]
#print(multiple_columns)


#index 2 and 10 for nets and knicks
df.loc[2]


# In[51]:


df = df.reset_index()


# In[58]:


#win % 2015-2019 szns 
#Nets 2 & Knicks 10
df.reset_index(inplace=True, drop=True)
df2 = df.iloc[[2, 10], df.columns.get_indexer(['w_pct_2015', 'w_pct_2016', 'w_pct_2017', 'w_pct_2018'])]


# In[57]:


print(df)

