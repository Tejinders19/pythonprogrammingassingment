#!/usr/bin/env python
# coding: utf-8

# <h4>1. Write a Python program to print &quot;Hello Python&quot;?
# 

# In[1]:


print("Hello Python")


# <h4>2. Write a Python program to do arithmetical operations addition and division.?

# In[10]:


a=float(input("enter any 1st natural no"))
b=float(input("enter any  2nd natural no"))
print(a+b)
print(a/b)


# <h4>Write a Python program to find the area of a triangle?

# In[12]:


import math
a=float(input("enter the first side of triangle"))
b=float(input("enter the second side of triangle"))
c=float(input("enter the third side of triangle"))
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
print(math.sqrt(area))


# <h4>Write a Python program to swap two variables?

# In[18]:


a=float(input("enter first no"))
b=float(input("enter second no"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)


# <h4>Write a Python program to generate a random number?

# In[20]:


import random as n
a=n.random()
print(a)


# In[ ]:




