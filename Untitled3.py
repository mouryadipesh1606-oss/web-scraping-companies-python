#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[7]:


headers = {
    'User-Agent' : 'Mozilla/5.0'
}


# In[8]:


page = requests.get(url, headers=headers)


# In[9]:


table = BeautifulSoup(page.text , 'html')


# In[12]:


dtable = table.find('table', class_ ='wikitable sortable')


# In[13]:


dtable


# In[19]:


header = dtable.find_all('th')


# In[21]:


title =[h.text.strip() for h in header]


# In[22]:


title


# In[39]:


import pandas as pd


# In[40]:


df = pd.DataFrame(columns= title)


# In[41]:


df


# In[42]:


rows = dtable.find_all('tr')


# In[43]:


rows


# In[44]:


for row in rows[1:] :
    cols = row.find_all('td')
    data = [col.text.strip() for col in cols]
    df.loc[len(df)] = data


# In[32]:





# In[45]:


df


# In[47]:


df.to_csv('C:/Users/Public/Documents/Companies.csv', index= False)


# In[ ]:




