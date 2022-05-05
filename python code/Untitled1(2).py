#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


df.shape

df.dropna(inplace = True)

print(df.to_string()) 


# In[3]:


df.isnull().sum()


# In[4]:


df.describe()


# In[5]:


plt.figure(figsize=(15,15))

plt.plot(df.w_pct_2015, df.team_name_2015, label="2015-16", color="#216331", marker="o")
plt.plot( df.w_pct_2016, df.team_name_2016, label="2016-17", color="#008b91", marker="o")
plt.plot(df.w_pct_2017, df.team_name_2017, label="2017-18", color="#45a8e4", marker="o")
plt.plot(df.w_pct_2018, df.team_name_2018, label="2018-19", color="#dcb8ff",marker="o")


plt.title("2015-2019 Eastern Conference Win %")
plt.xlabel("win %")
plt.legend()

plt.xticks(rotation=0)

plt.savefig("testing.png", dpi=100)


plt.show()


# In[138]:


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

plt.savefig("test1.png", dpi=100)


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

plt.savefig("test2.png", dpi=100)


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

plt.savefig("tests.png", dpi=100)


plt.show()



# In[6]:


df2 = df.iloc[[2, 10], df.columns.get_indexer(['team_name_2015','w_pct_2015', 'w_pct_2016', 'w_pct_2017', 'w_pct_2018'])]
df2


# In[23]:


df3 = df.iloc[[13], df.columns.get_indexer(['team_name_2015','w_pct_2015', 'w_pct_2016', 'w_pct_2017', 'w_pct_2018'])]
df3


# In[24]:


df4 = df.iloc[[1], df.columns.get_indexer(['team_name_2015','w_pct_2015', 'w_pct_2016', 'w_pct_2017', 'w_pct_2018'])]
df4


# In[ ]:





# In[ ]:





# In[141]:


#nyc stats 2015-19
import matplotlib.patches as mpatches

#pick bckground color
plt.rcParams['axes.facecolor'] = 'white'

XVals = ['Brooklyn Nets', 'New York Knicks']
YVals = [[ 0.256, 0.244, 0.341, 0.512],[0.390, 0.378, 0.354, 0.207]]

X = [XVals[i] for i, df2 in enumerate(YVals) for j in range(len(df2))]
Y = [val for df2 in YVals for val in df2]

colors = ['#917aff', '#00beff','#f1e0ff','#37f52a','#917aff', '#00beff','#f1e0ff','#37f52a']

#years
one_patch = mpatches.Patch(color='#917aff', label='2015-16')
two_patch = mpatches.Patch(color='#00beff', label='2016-17')
three_patch = mpatches.Patch(color='#f1e0ff', label='2017-18')
four_patch = mpatches.Patch(color='#37f52a', label='2018-19')

plt.legend(handles=[one_patch, two_patch, three_patch, four_patch])

plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.scatter(X, Y, marker='D', s = 180, color=colors, edgecolor="black")
plt.title("NY Team Stats 2015-19")
plt.xlabel('Team Name') 
plt.ylabel('Win %') 

plt.savefig("testio.png", dpi=100)

plt.show()
#make note of stark contrast btwn nets 2018-19 & knicks 2018-19


# In[143]:


df2.describe()


# In[165]:


df["w_pct_2015"].mean()


# In[166]:


# You can also iterate through rows
for index, row in df.iterrows():
    print(f"{index}\n{row}")
print()


# In[176]:


df.drop(['gp','gp.1','gp.2','gp.3'],axis=1).head()


# In[180]:


df['w_pct_2015'].mean()


# In[181]:


df['w_pct_2018'].mean()
#overall w_pct for eastern conf teams 
#seems to be lower
#than in 2015
#difference is 0.016


# In[194]:


df[df['w.1']>42].groupby(['team_name_2016', 'w.1']).mean()

#2016

#82 games played

#half of that is 41

#hawks, celtics, cavaliers, raptors, wizards 
#won more than 42 games in 2016


# In[205]:


#df.std()

#w_pct_2015     0.154290
#w_pct_2016     0.116585
#w_pct_2017     0.140876
#w_pct_2018     0.162024


# In[220]:


X = df[['w_pct_2015', 'w_pct_2016']]
y = df[['w_pct_2017', 'w_pct_2018']] 


from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_) 


# In[79]:


df

sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))


sns.set_color_codes("pastel")
sns.barplot(x="gp", y="team_name_2015", data=df,
            label="Total Games Played", color="#dcb8ff")

sns.set_color_codes("muted")
sns.barplot(x="w", y="team_name_2015", data=df,
            label="Games Won", color="#216331")

sns.set_color_codes("muted")
sns.barplot(x="l", y="team_name_2015", data=df,
            label="Games Lost", color="#45a8e4", alpha=.9)

ax.legend(ncol=3, loc="lower right", frameon=True)
ax.set(xlim=(0, 81), ylabel="",
       xlabel="", title="Eastern Conf. 2015-16")
sns.despine(left=True, bottom=True)

plt.savefig("15-16.png", bbox_inches="tight")


# In[6]:


#visualize the rest of the season underdogs?
df3 = df.iloc[[1, 2, 10, 12, 13], df.columns.get_indexer(['team_name_2015','w_pct_2015','team_name_2016','w_pct_2016', 'team_name_2017','w_pct_2017','team_name_2018','w_pct_2018',])]
df3


# In[68]:


df3 #atl div
sns.set_theme(style="white")



# Plot miles per gallon against horsepower with other semantics
sns.relplot(x="team_name_2015", y="w_pct_2015", hue="w_pct_2015", size="w_pct_2015",
            sizes=(100, 400), alpha=1, palette="muted",
            height=5.5, data=df3)
plt.xticks(rotation=10)

sns.relplot(x="team_name_2016", y="w_pct_2016", hue="w_pct_2016", size="w_pct_2016",
            sizes=(100, 400), alpha=1, palette="muted",
            height=5.5, data=df3)
plt.xticks(rotation=10)

sns.relplot(x="team_name_2017", y="w_pct_2017", hue="w_pct_2017", size="w_pct_2017",
            sizes=(100, 400), alpha=1, palette="muted",
            height=5.5, data=df3)
plt.xticks(rotation=10)

sns.relplot(x="team_name_2018", y="w_pct_2018", hue="w_pct_2018", size="w_pct_2018",
            sizes=(100, 400), alpha=1, palette="muted",
            height=5.5, data=df3)

plt.xticks(rotation=10)


# In[50]:


#visualize the rest of the season underdogs?
df4 = df.iloc[[4, 5, 6, 7, 9], df.columns.get_indexer(['team_name_2015','w_pct_2015','team_name_2016','w_pct_2016', 'team_name_2017','w_pct_2017','team_name_2018','w_pct_2018',])]
df4


# In[ ]:


df4 # central


# In[51]:


df5 = df.iloc[[0, 3, 8, 11, 14], df.columns.get_indexer(['team_name_2015','w_pct_2015','team_name_2016','w_pct_2016', 'team_name_2017','w_pct_2017','team_name_2018','w_pct_2018',])]
df5


# In[ ]:


df5 # southeast

