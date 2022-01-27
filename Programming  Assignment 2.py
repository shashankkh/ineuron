#!/usr/bin/env python
# coding: utf-8

# In[2]:


## 1.	Write a Python program to convert kilometers to miles?

kilometer=float(input("Enter Value of distance in kilometer"))
conversion_ratio=0.621371
miles=kilometer*conversion_ratio
print("Value of distance in miles:\n", miles)


# In[3]:


## 2.	Write a Python program to convert Celsius to Fahrenheit?

celsius = float(input("Enter Value of Celsius in centigrade "))
fahrenheit = (celsius * 1.8) + 32
print("Value of fahrenheit in centigrade:\n", fahrenheit)


# In[12]:


## 3.	Write a Python program to display calendar?

import calendar
yy=2022
print(calendar.calendar(yy))


# In[17]:


yy=2022
mm = 1
print(calendar.month(yy,mm))


# In[7]:


import math
def equationroot(a,b,c):
    d = b*b - 4*a*c
    sqrt_value = math.sqrt(abd(d))
    if d > 0:
        print("real and diffrent roots")
        print((-b+sqrt_val)/(2*a))
        print((-b-sqrt_val)/(2*a))
    elif d == 0:
        print(" real and same roots")
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = 1
b = 10
c = -24


if a == 0:
    ("Input correct quadratic equation")

else:
    equationroots(a, b, c)
        
        


# In[8]:


## Write a Python program to swap two variables without temp variable?

a = 7
b = 8

a,b = b, a


# In[9]:


a


# In[10]:


b


# In[ ]:




