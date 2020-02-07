#!/usr/bin/env python
# coding: utf-8

# Functions are used to perform a long process in a pecise an easy way.
# two types of funcion
# 1.Built in
# 2.pre defined fx

# # 1.Builtin fx

# Absolute function resturs the absolute value of the specified number.abs()

# all().Returns the true if all the items in an iterable are true.Otherwise t returns false. 

# asc11().it returns the readable version of any object.

# ascii(object),object may be list,tuple,strings etc.

# bool().returns boolean value of object

# enumerate().take an collection (eg tuple) and return it as na emunerate object.
# 

# format().formats a specified value into a specified format.

# getattr().returns the value of specified attribute from a specified object.

# Syntax:
# getattr(object,attribute,default)

# id().returns a unique id for a specified object.

# len().returns a number of items in an object.

# map().executes a specified fx for each items in an iterable.the item is sent to fx as a parameter.

# min().returns the item that have a lowest value in an iterable.

# pow().returns the vlaue of x to the power y ,x^y.

# setattr().sets teh vlaue of a speciied attribute of the specified object.

# sorted().returns the sorted list of the specified iterable objects.

# In[32]:


class person:
    name="faizan"
    age=24
    country="pakistan"
getattr(person,'age')    
    


# In[33]:


x=('true','true')
all(x)


# In[35]:


x=2
ascii(x)


# In[38]:


x=('false','false')
bool(x)


# In[39]:


x=('apple','bnnana')
enumerate(x)


# In[40]:


x=(0.5,'%')
format(x)


# In[43]:


id(x)


# In[44]:


len('apple')


# In[3]:


#map(function,iterable)
def myfun(n):
    return len(n)
x=map(myfun,('apple'))


# In[53]:


min(5,2,8)


# In[56]:


pow(2,3)


# In[68]:


class person:
    name="faizan"
    age=24
    country="pakistan"
setattr(person,'age',35)


# In[66]:


l1=[55,22,99]
sorted(l1)


# # 2.user defined functions

# In[5]:


def my_func(fname): #created a function with the parameter fname
    print(fname,"ashraf")  #print 
my_func("zeehsan")    #pass the argumment as fname


# In[8]:


def my_fun(country="Pakistan"):
    print("i am from"+country)
my_fun("kashmir") 
my_fun()


# In[12]:


def my_maths(x):
    return 5*x
print(my_maths(2))
print (my_maths(4))


# ## 2.1RECURSION

# Recursion is  a fx calling on itself.

# In[28]:


tri_rec=input(str("enter the value of k"))
def tri_rec(k):
    if(k>0):
        result=k+tri_rec(k-1)
        print(result)
    else:
        result=0
    return result


# ## 2.2 lamba() 

# it can take any num o arguments but can only have one expression.

# In[29]:


x=lambda a:a+5
print(x(5))


# In[30]:


x=lambda a,b,c:a+b+c
print(x(5,6,7))


# In[34]:


def myfunc(n): #takes n argument
    return lambda x:x*n   #this will return the value that is double or tripled
mydoubler=myfunc(2) #this store 2 in n
mytripler=myfunc(3) #his will store 3 in n

print(mydoubler(10))#this value multiply the x as 10 and double it after multiplying with 2
print(mytripler(10))#this value multiply the x as 10 and triple it after multiplying with 2


# In[44]:


def add():
    num1=int(input("enter ist num"))
    num2=int(input("enter 2nd num"))
print(num1+num2)


# ### positional arguments

# In[47]:


def add(a,b):
    print(a+b)
add(10,5,5)
#as two parameters were set a and b ,so we have to give teo arguments 


# In[48]:


def add(a,b):
    print(a+b)
add(10,5)
#positional arguments 


# In[49]:


def add(a,b):
    print(a+b)
add(b=10,a=5)


# ### key wod argument

# In[62]:


def fname(first,middle,last):
    print(first,middle,last)
fname("Muhammad","Faizan","Ashraf",)    


# In[65]:


def fname(first,middle,last):
    print(first,middle,last)
fname(first="Ashraf",middle="Muhammad",last"Ashraf")


# In[ ]:




