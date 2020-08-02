#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Program to find the greatest of two numbers
a=int(input('enter value for a: '))
b=int(input('enter value for b: '))
if(a>b):
    print('a is greater ')
elif(a<b):
    print('b is greater')
else:
    print('a and b are equal')


# In[12]:


#Program to find the smallest of two numbers
a=int(input('enter value for a: '))
b=int(input('enter value for b: '))
if(a<b):
    print('a is smaller ')
elif(a>b):
    print('b is smaller')
else:
    print('a and b are equal')


# In[13]:


#Program to find the smallest of three numbers
a=int(input('enter value for a: '))
b=int(input('enter value for b: '))
c=int(input('enter value for c: '))
if(a<b)and(a<c):
    print('a is the smallest of three numbers ')
elif(b<c)and(b<c):
    print('b is the smallest of three numbers')
else:
    print('c is the smalllest of three numbers')


# In[14]:


#Program to find weather a number is even or odd
a=int(input('enter value for a: '))
if(a%2==0):
    print('a is even')
else:
    print('a is odd')


# In[15]:


#Program to find weather is nubmer is positive, negative or zero
a=int(input('enter value for a: '))
if(a>0):
    print('a is positive')
elif(a<0):
    print('a is negative')
else:
    print('a is zero')


# In[16]:


#Program to find the blood match
donor=str(input("enter the blood group of donor A, B AB or O : "))
recipient=str(input('enter the blood group of recipient : '))
if(donor==recipient)or(donor=='O')or(recipient=='AB'):
    print('it is a match')
else:
    print('it is not a match')


# In[ ]:




