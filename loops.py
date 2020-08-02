#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loops
#average
n=int(input('enter a number:'))
sum=0
for n in range(1,n+1):
    sum+=n
avg=sum/n
print(avg)


# In[2]:


#factorial
n=int(input('enter a number:'))
fact=1
for n in range(1,n+1):
    fact*=n
print(fact)
    


# In[18]:


#prime or composite
n=int(input('enter a number:'))
for a in range(2,n):
    if(n%a==0):
        print('the number is composite')
    else:
         print('number is prime')
    break


# In[8]:


#sum of series
n=int(input('enter a number:'))
sum=0
for n in range(1,n+1):
    sum+=(1/n) 
print('the sum of the series is : ',sum)


# In[ ]:


#calender of a month
a=int(input('enter the start day:'))
b=int(input('enter the number of days in month:'))
for a in range(a,b+1):
    print(a)
    


# In[1]:


#nested loop
#pattern
for i in range(1,7):
    for j in range(1, i):
        print(j ,end='')
        j+=1
    print('\n',end='')
    


# In[2]:


#multiplication tables
for i in range(1,11):
    for j in range(1, 11):
        print(i, 'x', j, '=' ,i*j)
    print('\n',end='')


# In[4]:


#list and tuples
list=[1,2,3]
tuple=(1,2,3)
print(list)
print(tuple)
list=[1,2,1]
tuple=(1,2,1)
print(list)
print(tuple)


# In[5]:


#dictionary
dict={'a':1, 'b':2}


# In[6]:


dict


# In[11]:


#lists
l1=[1,2,3]
l2=[4,5,6]
l1+l2


# In[12]:


# can't multiply sequence by non-int of type 'list'


# In[15]:


#tuples
t1=(1,2,3,)
t1[0:2]


# In[2]:


a= int(input('Enter the first number:'))
b= int(input('Enter the second number:'))
print(a+b)


# In[4]:


x=3.14
int(x) 


# In[7]:


x=3
float(x)


# In[9]:


x=[1,2,3]
tuple(x) 


# In[10]:


x=[1,2,3]
str(x) 


# In[13]:


x=3
chr(x) 


# In[14]:


x='f'
ord(x) 


# In[ ]:





# In[ ]:




