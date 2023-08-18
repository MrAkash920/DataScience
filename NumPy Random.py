#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Generate a random number between 100 and 500
from numpy import random
import numpy as np
x = random.randint(100,500)
print (x)


# In[5]:


#generate random float
x = random.rand()
print(x)


# In[6]:


#genarate a 1-D array containing 5 random integers from 0 to 100
x = random.randint(100,size=(5))
print(x)


# In[7]:


#genarate a 2-D array containing 5 random integers from 0 to 100
x = random.randint(100,size=(3,5))
print(x)


# In[8]:


#genarate a 1-D array containing 5 random floats
x = random.rand(5)
print(x)


# In[9]:


#genarate a 2-D array containing 5 random floats
x = random.rand(3,3)
print(x)


# In[10]:


#choose a random value from an array
x = random.choice([1,3,6,9,12])
print(x)


# In[12]:


#geanerate a 2-D array that consists the values in the array parameter
x = random.choice([1,3,6,9,12],size=(3,5))
print(x)


# In[19]:


#genaerate a 1-D array containing 100 values where each value has to be 3,5,7,or 9
x = random.choice([3,5,7,9], p =[0.2,0.4,0.4,0.0],size=(100)) #sum of probility should be 1
print(x)


# In[20]:


#genaerate a 2-D array with 3 rows, containing 5 values where each value has to be 3,5,7,or 9
x = random.choice([3,5,7,9], p =[0.2,0.4,0.4,0.0],size=(3,5))
print(x)


# In[23]:


#shuffle array
arr = np.array([1,2,4,6,9])
random.shuffle(arr)
print(arr)


# In[25]:


#permutation of an array
arr = np.array([1,2,4,6,8])
print(random.permutation(arr))


# In[61]:


#Plotting a Distplot
import matplotlib.pyplot as plt
import seaborn as sb

sb.displot([0,1,2,3,4,6])
plt.show()


# In[66]:


#plotting distploat without histogarm
sb.distplot([0,3,6,9,12,15],kde = True, hist = False)
plt.show()


# In[31]:


#get a random normal distributiin of size 2*3
x = random.normal(size=(2,3))
print(x)


# In[32]:


#get a random normal distributiin of size 2*3 with mean at 1 and standard deviation at 2
x = random.normal(loc  = 1, scale = 2, size=(2,3))
print(x)


# In[35]:


#Visualization of normal distribution
sb.distplot(random.normal(size=500),hist = False)
plt.show()


# In[37]:


#Binomial Distribution
#Given 10 trials for coin toss generate 10 data points
x = random.binomial(n = 10, p = 0.5, size=10)
print (x)


# In[41]:


#visualization of binoomial distribution
sns.distplot(random.binomial(n = 10, p = 0.5, size=2000),hist = True, kde = False)
plt.show()


# In[69]:


#visualization of binoomial distribution
sb.kdeplot(random.binomial(n = 10, p = 0.5, size=2000))
plt.show()


# In[75]:


#distribution between Normal and binomial
sb.kdeplot(random.normal(loc = 50, scale = 5, size = 1000),label = 'Normal')
sb.kdeplot(random.binomial(n = 100, p = 0.5, size = 1000),label = 'Binomial')
plt.legend() #legend to show label
plt.show()


# In[57]:


import seaborn as sb
import numpy as np

data_normal = np.random.normal(loc=50, scale=5, size=1000)
data_binomial = np.random.binomial(n=100, p=0.5, size=1000)

sb.displot(data_normal, kde=True, label='Normal')
sb.displot(data_binomial, kde=True, label='Binomial')


# Additional plotting code as needed
plt.show()


# In[54]:


#Generate a random 1*10 distribution for occurence 2
x = random.poisson(lam = 2, size= 100)
print(x)


# In[71]:


#Visualization of Distribution
sb.displot(random.poisson(lam=2, size = 1000))
plt.show()


# In[73]:


#Difference between Noraml and Poisson Distribution
import matplotlib as mt
sb.kdeplot(random.normal(loc=50, scale= 5, size = 1000),label ='normal')
sb.kdeplot(random.poisson(lam = 50, size = 1000),label = 'poisson')
plt.legend()
plt.show()


# In[81]:


#distribution between binomial and poision
sb.kdeplot(random.binomial(n = 1000, p = 0.01, size = 1000), label = 'binomial')
sb.kdeplot(random.poisson(lam = 10, size = 1000), label = 'poisson')
plt.legend()
plt.show()


# In[84]:


#create a 2*3 uniform distribution
x = random.uniform(size=(2,3))
print(x)


# In[85]:


#visualize uniform distribution
sb.kdeplot(random.uniform (size=1000))
plt.show()


# In[86]:


#draw 2*4 sample from logistic distribution with mean at 1 and stddev 2.0
x = random.logistic(loc = 1, scale = 2, size=(2,4))
print(x)


# In[88]:


#visualize logistic distribution
sb.kdeplot(random.logistic(loc = 1, scale = 2, size=1000))
plt.show()


# In[89]:


#difference between normal and logistic distribution
sb.kdeplot(random.normal(scale= 2, size= 1000), label = 'normal')
sb.kdeplot(random.logistic(size= 1000), label = 'logistic')
plt.legend()
plt.show()


# In[90]:


#multinomial distribution
#draw out a sample for dice roll
x = random.multinomial(n = 6, pvals = [1/6,1/6,1/6,1/6,1/6,1/6])
print(x)


# In[91]:


#Exponential distribution
#draw out a sample for exponential distribution where 2.0 scale and 2*3 size
x = random.exponential(scale = 2, size=(2,3))
print(x)


# In[92]:


#visualization of exponential distribution
sns.kdeplot(random.exponential(size=1000))
plt.show()


# In[ ]:




