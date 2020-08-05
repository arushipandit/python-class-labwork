#!/usr/bin/env python
# coding: utf-8

# In[2]:


#* saves variables as vectors
def func(name, *fav_subject):
    print (name)
    for str in fav_subject:
        print(str)
func('a','b','c','4')


# In[3]:


#lambda functions
sum= lambda x,y:x+y
print('sum=',sum(3,5))


# In[7]:


def small(a,b):
    if(a>b):
        return a
    else:
        return b
sum=lambda x,y:x+y
dif=lambda x,y:x-y
print(small(sum(3,2),dif(1,3)))


# In[9]:


def increment(y):
    return (lambda x:x+1) (y)
a=100
print (a)
b=increment(a)
print('value after increment',b)


# In[10]:


twice= lambda x:x*2
print(twice(9))


# In[11]:


print((lambda x:x*2) (9))


# In[2]:


add= lambda x,y:x+y
multiply_and_add= lambda x,y,z: x* add(y,z)
print(multiply_and_add(2,3,4))


# In[9]:


#docstring
def func():
    """this is  a docstring"""
    return None
print('hi')
print(func.__doc__)
func()


# In[ ]:




