#!/usr/bin/env python
# coding: utf-8

# In[32]:


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
df = pd.read_csv("three_Untitled.csv", sep=",")


# In[33]:


df.shape

df.dropna(inplace = True)

print(df.to_string()) 


# In[34]:


df_2015 = df.iloc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], df.columns.get_indexer(['team_name_2015','3pm_2015','w'])]
df_2015


# In[71]:


df_2015[df_2015['w']>42].groupby(['team_name_2015', 'w']).mean()


# In[97]:


df_2015[df_2015['3pm_2015']>10].groupby(['team_name_2015', '3pm_2015']).mean()


# In[77]:


from statistics import mean


# In[78]:


one_scores = [9.9 , 8.7, 10.6, 10.7, 9.0, 8.1, 6.1, 8.6]


# In[79]:


mean(one_scores)


# In[80]:


df_2016[df_2016['w.1']>42].groupby(['team_name_2016', 'w.1']).mean()


# In[81]:


two_scores = [8.9 , 12, 13, 8.8, 9.2]


# In[82]:


mean(two_scores)


# In[83]:


df_2017[df_2017['w.2']>42].groupby(['team_name_2017', 'w.2']).mean()


# In[84]:


three_scores = [11.5, 12, 9, 11, 8.8, 11, 11.8, 9.9]


# In[85]:


mean(three_scores)


# In[86]:


df_2018[df_2018['w.3']>42].groupby(['team_name_2018', 'w.3']).mean()


# In[88]:


four_score = [12.6, 9.5, 13.5, 10.8, 12.4]


# In[89]:


mean(four_score)


# In[66]:


#df_2015.describe()
#df_2016.describe()
#df_2017.describe()
#df_2018.describe()


# In[ ]:





# In[35]:


df_2016 = df.iloc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], df.columns.get_indexer(['team_name_2016','3pm_2016','w.1'])]
df_2016


# In[36]:


df_2017 = df.iloc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], df.columns.get_indexer(['team_name_2017','3pm_2017','w.2'])]
df_2017


# In[37]:


df_2018 = df.iloc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], df.columns.get_indexer(['team_name_2018','3pm_2018','w.3'])]
df_2018


# In[31]:


pip install chart_studio


# In[ ]:





# In[51]:


import plotly

plotly.offline.init_notebook_mode()
df = df_2015
fig = px.line(df, x='3pm_2015', y='w', color='team_name_2015', symbol="3pm_2015")
fig.update_traces(marker=dict(size=15))
fig.show()


plotly.offline.plot(fig, filename = 'filename.html', auto_open=False)



# In[47]:


import plotly
import chart_studio.tools as tls

plotly.offline.init_notebook_mode()
df = df_2016
fig = px.line(df, x='3pm_2016', y='w.1', color='team_name_2016', symbol="3pm_2016")
fig.update_traces(marker=dict(size=15))
fig.show()


plotly.offline.plot(fig, filename = 'filename1.html', auto_open=False)



# In[48]:


import plotly
import chart_studio.tools as tls

plotly.offline.init_notebook_mode()
df = df_2017
fig = px.line(df, x='3pm_2017', y='w.2', color='team_name_2017', symbol="3pm_2017")
fig.update_traces(marker=dict(size=15))
fig.show()


plotly.offline.plot(fig, filename = 'filename2.html', auto_open=False)



# In[49]:


import plotly
import chart_studio.tools as tls

plotly.offline.init_notebook_mode()
df = df_2018
fig = px.line(df, x='3pm_2018', y='w.3', color='team_name_2018', symbol="3pm_2018")
fig.update_traces(marker=dict(size=15))
fig.show()


plotly.offline.plot(fig, filename = 'filename4.html', auto_open=False)



# In[101]:


df_2015[df_2015['w']<20].groupby(['team_name_2015', 'w']).mean()


# In[103]:


df_2016[df_2016['w.1']<28].groupby(['team_name_2016', 'w.1']).mean()


# In[109]:


df_2018[df_2018['w.3']<25].groupby(['team_name_2018', 'w.3']).mean()


# In[110]:


df


# In[120]:





# In[ ]:




