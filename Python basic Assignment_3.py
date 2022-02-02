#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 1. Why are functions advantageous to have in your programs?

## Ans. Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.


# In[ ]:


## 2. When does the code in a function run: when it's specified or when it's called?
## Ans. The code in a function executes when the function is called.


# In[ ]:


## 3. What statement creates a function?

## Ans. The def statement creates a function.


# In[ ]:


## 4. What is the difference between a function and a function call?

## Ans.The concept of function has been introduced to eliminate this repetition of same task while Using a function to do a particular task any point in program is called as function call.


# In[2]:


## 5. How many global scopes are there in a Python program? How many local scopes?
## Ans. There is one global scope, and a local scope is created whenever a function is called
var='global scope'
def my_function():
    var='local scope'
    print(var)
my_function()
print(var)


# In[ ]:


## 6. What happens to variables in a local scope when the function call returns?
## Ans. When a function returns, the local scope is destroyed, and all the variables in it are forgotten. we will not be able to access the out side the function


# In[ ]:


## 7. What is the concept of a return value? Is it possible to have a return value in an expression?
## Ans. A return value is the value that a function call evaluates to. A return value can be used as part of an expression, Like any value.


# In[ ]:


##8.If a function does not have a return statement, what is the return value of a call to that function?
## Ans. If there is no return statement for a function, its return value is None


# In[ ]:


##9. How do you make a function variable refer to the global variable?
## Ans. By representing a valible by global keywaord in the body of a function Example : global a


# In[ ]:


## 10. What is the data type of None?
## Ans. The data type of none is NoneType


# In[4]:


## 11. What does the sentence import areallyourpetsnamederic do?
## Ans. areallyourpetsnamederic ia not a python module. Importing this module will throughs ModuleNotFoundError exception.

import areallyourpetsnamederic


# In[ ]:


## 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
## Ans.This function can be called with spam.bacon(). like below
    import spam
    spam.bacon()


# In[ ]:


## 13. What can you do to save a programme from crashing if it encounters an error?
## Ans. we can write lines of code in try block. This will not crash the programme. And in except block we can catch the exception. 


# In[ ]:


## 14. What is the purpose of the try clause? What is the purpose of the except clause?
## Try : The code that could potentially cause an error goes in the try clause.
## except : The code that executes if an error happens goes in the except clause, like print statments about exceptions.

