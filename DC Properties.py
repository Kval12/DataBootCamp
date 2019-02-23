#!/usr/bin/env python
# coding: utf-8

# In[52]:


#PANDA
import pandas as pd


# In[53]:


#Get Data
location = "datasets/DC_Properties.csv"
df = pd.read_csv(location)


# In[54]:


df.head()


# In[ ]:





# In[55]:


df.drop('Unnamed: 0', axis=1)


# In[34]:


df1 = df.drop('Unnamed: 0', axis=1)


# In[35]:


df1.columns


# In[38]:


dupe = df1.duplicated(['FULLADDRESS'],keep='last') 
df1[dupe]


# In[39]:


df1.drop_duplicates()


# In[40]:


df2=df1.drop_duplicates()


# In[65]:


df2.groupby('QUADRANT')['PRICE'].min()


# In[59]:


print(df2)


# In[62]:


copydf.groupby('QUADRANT')['PRICE'].median()


# In[64]:


pd.pivot_table(copydf, values=['PRICE'], index=['QUADRANT'])


# In[63]:


copydf.describe()


# In[57]:


meangrade = df2['PRICE'].mean()
stdgrade = df2['PRICE'].std()
toprange = meangrade + stdgrade * 1.96
botrange = meangrade - stdgrade * 1.96

copydf = df2.copy() #to not mess up the original df
copydf = copydf.drop(copydf[copydf['PRICE'] > toprange].index)
copydf = copydf.drop(copydf[copydf['PRICE'] < botrange].index)


# In[58]:


print(copydf)


# In[49]:


copydf.sort_values('PRICE')


# In[56]:


copydf.max()


# In[60]:


df2.max()


# In[61]:





# In[ ]:




