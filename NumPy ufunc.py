#!/usr/bin/env python
# coding: utf-8

# In[2]:


#zip() function (Python in-built function)
x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = []
for i , j in zip(x,y):
    z.append(i+j)
print(z)


# In[4]:


#numpy has ufunc for the abve same problem called, add(x,y)
import numpy as np
a = [1,2,3,4]
b = [5,6,7,8]
c = np.add(a,b)
print(c)


# In[5]:


#craete your ufunc for multiplication
#use frompyfunction
def mymulti(a,b):
    return a * b
mymulti = np.frompyfunc(mymulti,2,1)
print(mymulti([1,2,3,4],[5,6,7,8]))


# In[7]:


#to check wether the function is ufunc or not
print(type(np.add))
print(type(np.concatenate))


# In[8]:


#Simple Arthematic
#Add the values of arr1 and arr2
arr1 = np.array([10,12, 15, 24])
arr2 = np.array([12,19, 20, 19])

arr3 = np.add(arr1,arr2)
print(arr3)


# In[9]:


#Subtract the values of arr1 amd arr2
arr1 = np.array([20,30,40,50])
arr2 = np.array([17,22,35,40])

arr3 = np.subtract(arr1,arr2)
print(arr3)


# In[10]:


#Multiply the values of arr1 amd arr2
arr1 = np.array([20,30,40,50])
arr2 = np.array([17,22,35,40])

arr3 = np.multiply(arr1,arr2)
print(arr3)


# In[12]:


#Devide the values of arr1 amd arr2
arr1 = np.array([20,30,40,50])
arr2 = np.array([2,15,5,40])

arr3 = np.divide(arr1, arr2)
print(arr3)


# In[13]:


#raise the values in arr1 to the power of values in arr2
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])

arr3 = np.power(arr1,arr2)
print(arr3)


# In[14]:


#return reminder using mod()
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])

arr3 = np.mod(arr1,arr2)
print(arr3)


# In[15]:


#return reminder using reminder()
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])

arr3 = np.mod(arr1,arr2)
print(arr3)


# In[16]:


#return quotient with mod using divmod()
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])

arr3 = np.divmod(arr1,arr2)
print(arr3)


# In[18]:


#return the quotient and mod
arr = np.array([-1,-2,1,2,3,-4])
newarr = np.abs(arr)
print(arr)


# In[19]:


#Truncate elemante of the following array
arr = np.trunc([-3.1666,3.6667])
print(arr)


# In[21]:


#Fix elemante of the follwing array
#Note* Truncate and fix works same
arr = np.fix([-3.1666, 3.6667])
print(arr)


# In[23]:


#Round of 4.2666 to 2 decimal
arr = np.around(4.2666, 2)
print(arr)


# In[31]:


#Floor the element of the following array
arr = np.floor([-3.1666, 3.6667])
print(arr)


# In[32]:


#Ceil the element of the following array
arr = np.ceil([-3.1666, 3.6667])
print(arr)


# In[34]:


#Find log at base 2 of all elements of following array
arr = np.arange(1,10)
print(np.log2(arr))


# In[35]:


#Find log at base 10  of all elements of following array
arr = np.arange(1,10)
print(np.log10(arr))


# In[36]:


#Find log at base e
arr = np.arange(1,10)
print(np.log(arr))


# In[38]:


#Find log at any base using frompyfunc() and math.log()
from math import log
nplog = np.frompyfunc(log,2,1)
print(nplog(100,15))


# In[39]:


#sum the values in arr1 and the values in arr2
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

newarr = np.sum([arr1,arr2])
print(newarr)


# In[40]:


#perform summation in the following array over the 1st axis
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

newarr = np.sum([arr1,arr2], axis = 1)
print(newarr)


# In[41]:


#perform cummulative sum using cumsum() function
arr = np.array([1,2,3])
newarr = np.cumsum(arr)
print(newarr)


# In[44]:


#find product of elements in an array
arr = np.array([1,2,3,4])
x = np.prod(arr)
print(x)


# In[45]:


#find product of elements of arr1 and arr2 in an array
arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
x = np.prod([arr1,arr2])
print(x)


# In[46]:


#product over axis=1
arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
x = np.prod([arr1,arr2],axis=1)
print(x)


# In[49]:


#cummulative product
arr1 = np.array([1,2,3,4,5])
x = np.cumprod(arr1)
print(x)


# In[51]:


#compute discrete differences of the following array
arr = np.array([10,15,25,40])
newarr = np.diff(arr)
print(newarr)


# In[52]:


#compute discrete difference of the folllowing array twice
arr = np.array([10,15,25,40])
newarr = np.diff(arr,n=2)
print(newarr)


# In[54]:


#finding lcm of two number
num1 = 10
num2 = 12
x = np.lcm(num1,num2)
print(x)


# In[55]:


#find the lcm of the values of the following array
arr = np.array([3,6,9])
x = np.lcm.reduce(arr)
print(x)


# In[56]:


#find the lcm of the values of the following array
arr = np.arange(1,11)
x = np.lcm.reduce(arr)
print(x)


# In[57]:


#finding GCD or HCF of two number
num1 = 10
num2 = 12
x = np.gcd(num1,num2)
print(x)


# In[59]:


#find the gcd of the values of the following array
arr = np.array([3,6,9,18,27])
x = np.gcd.reduce(arr)
print(x)


# In[64]:


#Find  sine value of PI/2
x  = np.sin(np.pi/2)
print(x)


# In[65]:


#Find sine value for all of the values in array
arr = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x = np.sin(arr)
print(x)


# In[66]:


#convert all of the values in the folloeing array arr to radians
arr = np.array([90,180,270,360])
x = np.deg2rad(arr)
print(x)


# In[68]:


#convert all of the values in the folloeing array arr to degree
arr = np.array([np.pi/2,np.pi,1.5*np.pi/4,np.pi/5])
x = np.rad2deg(arr)
print(x)


# In[72]:


#find the angle of sine values 1.0
x = np.arcsin(1.0)
print(x)


# In[73]:


#find the angle of tan values of 5.0
x = np.arctan(5.0) #arccos() for cos values
print(x)


# In[74]:


#find the angle for all the sine values in the array
arr = np.array([1,-1,0.1])
x = np.arcsin(arr)
print(x)


# In[75]:


#Find the hypotenues for 4 base and 3 perpendicular
base = 4
perp = 3
x = np.hypot(base,perp)
print(x)


# In[76]:


#Find sinh values of PI/2
x = np.sinh(np.pi/2)
print(x)


# In[77]:


#Find the cosh values for all the values in arr
arr = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x = np.cosh(arr)
print(x)


# In[78]:


#Find the angle of 1.0
x = np.arcsinh(1.0)
print(x)


# In[79]:


#Find the angle for all tanh values
arr = np.array([0.1,0.2,0.5])
x = np.arctanh(arr)
print(x)


# In[80]:


#convert folloeing array with the repeted elements to a set
arr = np.array([1,1,1,2,3,4,5,5,6,7])
x = np.unique(arr)
print(x)


# In[81]:


#Find union of the following two sets
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
x = np.union1d(arr1,arr2)
print(x)


# In[83]:


#Find intersection of the following two sets
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
x = np.intersect1d(arr1,arr2)
print(x)


# In[84]:


#Find the set difference of set1 and set2
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setdiff1d(set1,set2,assume_unique=True)
print(newarr)


# In[86]:


#Find the symmetric difference of set1 and set2
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setxor1d(set1,set2,assume_unique=True)
print(newarr)


# In[ ]:





# In[ ]:




