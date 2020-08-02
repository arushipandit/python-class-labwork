#!/usr/bin/env python
# coding: utf-8

# In[4]:


#factorial using function
def factorial(i):
    fact=1
    for i in range(1,i+1):
         fact*=i
    return fact
i=int(input('enter a number for factorial:'))
print(factorial(i))
#there is a inbuilt function for factorial in math library


# In[7]:


#maximun marks out of five student
def maxmarks(i):
    input=()
    marks = [0]
    inpt = input("Enter the marks for 5 students: ").strip().split()
    for i in inpt:
        i=int(i)
        marks.append(i)
    print("The maximum marks scored are",max(marks),"by student",marks.index(max(marks)))


# In[12]:


var='good'
def display():
    global var
    var="morning"
    print(var)
display()
print(var)
var='nice day'
print(var)


# In[11]:


def display(name,course='ai'):
    print('name=',name)
    print('course=',course)
display(course='bca',name='teena')
display(name='reena')


# In[ ]:




