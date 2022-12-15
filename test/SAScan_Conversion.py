#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy


# In[9]:


# Import data
filepath= ("test/SAscan.csv")


# In[10]:


# Read in data
dataframe = pd.read_csv("SAscan.csv", names=["freq"])


# In[11]:


# Split data using ; as delimiter
dataframe=dataframe["freq"].str.split(";", expand=True)

# Name headers
dataframe.rename(columns={0:"freq", 1: "level"}, inplace=True)


# In[12]:


# Convert freq column to double/float variable type
dataframe["freq"] = pd.to_numeric(dataframe["freq"])
dataframe["level"] = pd.to_numeric(dataframe["level"])

dataframe=dataframe.astype(float)

#Divide Freq column
dataframe["freq"]=dataframe["freq"]/1000000


# In[13]:


# Round Freq and Level columns to respective decimal places
roundfreq= dataframe['freq'] = dataframe['freq'].round(3)
roundlevel= dataframe['level'] = dataframe['level'].round(2)

# concatenate dataframes
Updated_SAscan = pd.concat([roundfreq, roundlevel], axis= 1)


# In[14]:


Updated_SAscan.to_csv('./newfile/Updated_SAscan.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




