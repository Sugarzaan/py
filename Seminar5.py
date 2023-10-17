#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myfunction(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()
myfunction(6)


# In[2]:


def myfunction(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()
myfunction(6)


# In[5]:


dict1 = {'Bat':25,'Oyun':29, 'Dulam':19, 'Suren':31}
def func2(dict):
        maxkey = max(dict, key=dict.get)
        minkey = min(dict, key=dict.get)
        return maxkey, minkey
func2(dict1)


# In[4]:


import numpy as np
x=(np.arange(1,1000))
sum=0
for i in x:
    if((i%3==0) | (i%7==0)):
        sum += i;
print(sum)


# In[ ]:




