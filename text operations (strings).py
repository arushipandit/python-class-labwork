#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to convert all characters in lower case
str=input('enter a  paragraph of around 200 words:')
print('the paragraph in lower case is')
print(str.lower())


# In[4]:


#to count total number of words in paragraph
str=input('enter a  paragraph of around 200 words:')
print("The number of words in string are : ", len(str.split()))


# In[12]:


#removing the words like 'the , in , on, are, a, with, from' and counting the words after removing
str=input('enter a  paragraph of around 200 words:')
str=str.replace('the', '')
str=str.replace('in', '')
str=str.replace('are', '')
str=str.replace('on', '')
str=str.replace('a', '')
str=str.replace('with', '')
str=str.replace('from', '')
print(str)
print("The number of words in string are : ", len(str.split()))


# In[3]:


#number of duplicates
str=input('enter a  paragraph of around 200 words:')
count = dict()
word = str.split()
for i in word:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print('words repeated:',count)


# In[ ]:





# In[ ]:




