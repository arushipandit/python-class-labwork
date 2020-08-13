#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str=input('enter a  string:')
print(str)


# In[ ]:


print()
print("Good", end=" ")
print("Morning")


# In[2]:


str='this is to test string methodes'
print(str.capitalize())
print(str.center(12, '*'))
print(str.zfill(10))
print(str.lower())
print(str.upper())
print(str.lstrip())
print(str.rstrip())
print(str.strip())
print(min(str))
print(max(str))
print(str.replace('test', 'see'))
print(str.title())
print(str.swapcase())
print(str.split(','))
print('/'.join(str))
print(str.isidentifier())
print(list(enumerate(str)))


# In[ ]:


'vi' in 'victory'


# In[ ]:


str1='this is a python class'
str2='python'
if str2 in str1:
    print('present')
else:
     print('not present')


# In[ ]:


if str2 not in str1:
    print('not present')
else:
     print('present')


# In[ ]:


str1='this is a python class'
i=0
while i<len(str1):
    letter=str1[i]
    print(letter)
    i=i+1


# In[3]:


program ='B.tech AI'

batch=2023

print('my program is %s and batch is %d',(program, batch))


# In[ ]:


#does the string have vowels
str1=input('enter a  string:')
'a' or 'e' or 'i' or 'o' or 'u' in str1
print('present')


# In[ ]:


#does the string have vowels print the position also
vowels=['a','e','i','o','u']
str1=input('enter a  string:')
if volwels in str1:
    print(i,'is at position',)


# In[ ]:





# In[ ]:


user=input('enter username:')
password=input('enter username:')
print(user)
for i in (0,len(password)):
    print(password.replace(i,'*'))


# In[ ]:


str1='this is a python class'
i=0
while i<len(str1):
    letter=str1[i]
    print(letter)
    i=i+1


# In[ ]:


str='    hello'
print(str.lstrip())
print(str.rstrip())
print(max(str))
print(str.strip())

