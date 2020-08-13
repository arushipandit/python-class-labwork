#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Arushi Pandit
def display(**kwarg):
    for i in kwarg:
        print(i)
display(emp='kelly',salary=9000)
#here only emp and salary are printed because **kwargs take arguments as a dictionary 
#to display kelly and 9000
def display(**kwargs):
    for i,j in kwargs.items():
        print(i,j)


# In[4]:


#Arushi Pandit
def outerfun(a1,b1):
    def innerfun(c1,d1):
        return c1+d1
    return a1
    return innerfun(a1,b1)
res=outerfun(5,10)
print(res)


# In[ ]:


def fun1(num):
    return num +25
fun1(5)
print(num)


# In[ ]:


def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)


# In[ ]:


#module
import MyFactorial
n=int(input('enter a number:'))
print('factorial ',MyFactorial.fact(n))


# In[ ]:


def fun1(num):
    return 
n=fun1(5)
print(n)


# In[ ]:


def fun1(num):
    return num+2, num+3
x,y=fun1(5)
print(x,y)


# In[ ]:


def fun1(num):
    return num+2, num+3
x=fun1(5)
print(x)


# In[ ]:


def fun1():
    x=100
x=fun1()
print(x)

