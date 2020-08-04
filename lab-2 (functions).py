#!/usr/bin/env python
# coding: utf-8

# In[1]:


#find cube of a number using function with parameters
def cube(num):
    c=num*num*num
    return c
num=int(input('Enter a number :'))
print('cube is :',cube(num))


# In[5]:


#find cube of a number using function without parameters
def cube():
    num=int(input('Enter a number :'))
    c=num*num*num
    return c
print('cube is :',cube())


# In[ ]:


#calculate area of circle with parameters
def area(radius):
    ar=3.14*radius*radius
    return ar
radius=int(input('Enter the radius of circle :'))
print('area is :',area(radius))


# In[ ]:


#calculate area of circle without parameters
def area():
    radius=int(input('Enter the radius of circle :'))
    ar=3.14*radius*radius
    return ar
print('area is :',area())


# In[7]:


#calculate sum of numbers from n1 to n2 with parameters
def sum_of_num(n1,n2):
    s=0
    for i in range(n1,n2):
        s+=i
    return s
n1=int(input('Enter the lower bound for sum :'))
n2=int(input('Enter the upper bound for sum :'))
print('The sum in this range is :',sum_of_num(n1,n2))


# In[5]:


#calculate sum of numbers from n1 to n2 without parameters
def sum_of_num(n1,n2):
    s=2
    n1=int(input('Enter the lower bound for sum :'))
    n2=int(input('Enter the upper bound for sum :'))
    for i in range(n1,n2):
        s+=i
    return s
print('The sum in this range is :',sum_of_num(n1,n2))


# In[1]:


#calculate sum of numbers from n1 to n2 with keyword parameters
def sum_of_num(n1,n2):
    s=0
    for i in range(n1,n2):
        s+=i
    return s
print(sum_of_num(n2=10,n1=2))


# In[4]:


#calculate sum of numbers from n1 to n2 with default parameters
def sum_of_num(n1,n2=5):
    s=0
    for i in range(n1,n2):
        s+=i
    return s
print('The sum in this range is :',sum_of_num(n1=1))
print('The sum in this range is :',sum_of_num(n1=0,n2=7))


# In[2]:


#Function to concatenate two strings with parameters
def concat(s1,s2):
    s=s1+s2
    return s
s1=input('Enter the first string :')
s2=input('Enter the second string :')
print('The resultant string is :',concat(s1,s2))


# In[3]:


#Function to concatenate two strings keyword arguments
def concat(s1,s2):
    s=s1+s2
    return s
print('The resultant string is :',concat(s2='hii',s1='how r u'))


# In[9]:


#Function to concatenate two strings default arguments
def concat(s1,s2='good morning'):
    s=s1+s2
    return s
print('The resultant string is :',concat(s1='hii'))


# In[ ]:




