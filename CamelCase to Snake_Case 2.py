
# coding: utf-8

# # To Convert a camelCase form into a user-friendly field name.

# In[1]:


import pandas as pd


# In[18]:


def getter(text):
    result=[]
    pos=0
    #checks if text starts with get and has alphabets only
    if text.startswith('get') and text.isalpha():
    #stores the text starting from the 4th character in variable called string
        string=text[3:]
    else:
        return print('Wrong Format')
    #checks if the position of the alphabet is less than the length of string
    while pos < len(string): 
    #checks if the alphabet is in upper case
        if string[pos].isupper():
                if pos-1 > 0 and string[pos-1].islower() or pos-1 > 0 and pos+1 < len(string) and string[pos+1].islower():
                    result.append("_%s" % string[pos])
                else:
                    result.append(string[pos])
        else:
            result.append(string[pos])
    #adds 1 to pos and assigns the value to pos
        pos+=1
    #joining with empty separators
    return "".join(result)


# In[19]:


getter('getCurrency')


# In[16]:


getter('getAccountName')


# In[5]:


getter('getLongAccountName')


# In[6]:


getter('getTradeID')


# In[11]:


getter('getSWIFTCode')


# In[12]:


getter('get1234')


# In[17]:


getter('1234')

