#!/usr/bin/env python
# coding: utf-8

# In[1]:


#calculate area of a circle
r=int(input('enter the radius of circle: '))
print('the area of circle is : ', 3.14*r*r)


# In[2]:


#Calculate area of a triangle
h=int(input('enter the height of triangle: '))
b=int(input('enter the base of triangle: '))
print('the area of triangle is : ', 0.5*b*h)


# In[3]:


#Calculate distance between two points
x1=int(input('enter the x-coordinate of first point: '))
y1=int(input('enter the y-coordinates of first point: '))
x2=int(input('enter the x-coordinate of second point: '))
y2=int(input('enter the y-coordinates of second point: '))
r=((x1-x2)**2+(y1-y2)**2)**0.5
print('the distance between the points is : ',r )


# In[4]:


#Calculate bill amount for an item given its quantity sold, price of an item, discount and tax
q=int(input('enter the quantity of the item: '))
p=int(input('enter the price of the item: '))
d=int(input('enter the discount on the item in percentage: '))
t=int(input('enter the tax on the item in percentage: '))
b=q*(p*(1-0.01*(d-t)))
print('the bill amount is : ',b )


# In[8]:


#Calculate a student’s result based on two examinations, 1 sports event, and 3 activities conducted.
#The weightage of activities = 30%, sports = 20% and examination =50% 
e1=int(input('enter the marks of first examination: ')) 
e2=int(input('enter the marks of second examination: ')) 
s=int(input('enter the marks of sports: ')) 
a1=int(input('enter the marks of first activity: ')) 
a2=int(input('enter the marks of second activity: ')) 
a3=int(input('enter the marks of third activity: ')) 
e=(e1+e2)/2 
a=(a1+a2+a3)/3 
marks= (s*0.2)+(e*0.5)+(a*0.3) 
print('the result in percentage is : ',marks)


# In[9]:


#Write a program to swap two numbers
a=int(input('enter value for a : '))
b=int(input('enter value for b : '))
t=a
a=b
b=t
print('the value of a after swappping is : ',a)
print('the value of b after swappping is : ',b)


# In[10]:


#Write a program to read a character in uppercase and then print it in lowercase
a=str(input('enter a string : '))
print('This is the string entered : ',a)
b=a.lower()
print('This is the string in lowercase : ',b)


# In[11]:


#Write a program to calculate number of seconds in a day
a=int(input('enter number of days : '))
s=a*24*60*60
print('Seconds in {} days are : {} '.format(a,s))


# In[13]:


#Write a program that accepts an object’s mass (in kilograms) and velocity (in meters per second) and displays its momentum.
m=int(input('enter the mass of object in kg : '))
v=int(input('enter the velocity of the object in meters per second : '))
p=m*v
print('The momentum of the object is {} kg.m/s'.format(p))


# In[ ]:




