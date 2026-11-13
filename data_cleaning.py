#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("Desktop/Superstore_Sales_Analysis/dataset/Book1.csv")


# In[3]:


df.head()


# In[48]:


df.shape


# # what is missing

# In[49]:


df.isnull().sum()


# In[50]:


(df.isnull().sum()/df.shape[0])*100


# In[51]:


df.isnull().sum().sum()


# In[52]:


(df.isnull().sum().sum()/df.shape[0]*df.shape[1])*100


# In[53]:


sns.heatmap(df.isnull())
plt.show()


# # handling missing values

# # (VALUE DROPPING)
# 

# In[54]:


#if error more then 50% then drop the cloumn


# In[56]:


df.drop(columns=['Salary'], inplace=True)


# In[57]:


df.shape


# In[58]:


df.dropna()


# In[62]:


df.dropna(inplace= True)


# In[63]:


df.isnull().sum()


# In[64]:


df.shape


# # (IMPUTING CATEGORY DATA)

# In[4]:


df = pd.read_csv("Desktop/Superstore_Sales_Analysis/dataset/Book1.csv")
df.head()


# In[5]:


df.shape


# In[9]:


df.isnull().sum()


# In[8]:


df.fillna(10 ) #now in all null area we get 10


# # Forward fillling and backward filling

# In[11]:


df.fillna(method="ffill",axis=1)


# # Mode

# In[ ]:




