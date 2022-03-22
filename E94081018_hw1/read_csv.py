#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
dataset = pd.read_csv("./dataset.csv")


# In[8]:


pd.DataFrame(dataset)


# In[9]:


pd.DataFrame(dataset.nlargest(10, "Income"))


# In[ ]:




