
# coding: utf-8

# # To Convert a camelCase form into a user-friendly field name.

# In[23]:


import pandas as pd


# In[1]:


def getter(text):
    result = []
    pos = 0
     #checks for the position of the alphabet, checks if it starts with get and if the input text is string
    while pos < len(text) and text.startswith('get') and text.isalpha():
        if text[pos].isupper():
            if pos-1 > 0 and text[pos-1].islower() or pos-1 > 0 and             pos+1 < len(text) and text[pos+1].islower():
                result.append("_%s" % text[pos])
            else:
                result.append(text[pos])
        else:
            result.append(text[pos])
        pos +=1
    # joins all chars into one string
    string_joined = "".join(result)
    # splits string by _ and returns all strings after first position, converts list into string with _
    return "_".join(string_joined.split('_')[1:])


# In[2]:


getter('getCurrency')


# In[11]:


getter('getAccountName')


# In[12]:


getter('getLongAccountName')


# In[13]:


getter('getTradeID')


# In[14]:


getter('getSWIFTCode')


# In[3]:


getter('get1234')


# In[4]:


getter('currency')

