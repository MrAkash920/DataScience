#!/usr/bin/env python
# coding: utf-8

# In[1]:


#starting Numpy
import numpy
arr = numpy.array([1,2,3,4,5])
print(arr)


# In[2]:


#Numpy as np
import numpy as np;
arr = np.array([10, 20, 30, 40])
print(arr)


# In[3]:


#checking numpy version
print (np.version)


# In[4]:


#print type of array
print(type(arr))


# In[6]:


#Use tuple to create a NumPy array
arr1 = np.array((1,2,3,4,5))
print(arr1)


# In[11]:


#2d arrays
arr2 = np.array([[1,2], [3,4]])
print(arr2)


# In[16]:


#3d arrays
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print(arr3)


# In[14]:


#print the number of dimension
a = np.array(42)
b = np.array([1,2,3,4])
c = np.array([[1,2], [3,4]])
d = np.array([[[1,2,3],[4,4,6]],[[7,8,9],[1,2,3]]])
print (a.ndim) #ndim is an attribute is used to print the number of dimension
print (b.ndim)
print (c.ndim)
print (d.ndim)


# In[18]:


#Crate an array with any number of dimension and verify it by print the dimension
arr = np.array([1,2,3,4], ndmin = 5) #ndmin is used to create n dimnesional array
print (arr)
print("Number of dimensions: ", arr.ndim)


# In[21]:


#Array indexing
arr = np.array([1,2,3,4])
print (arr[1])
print (arr[1] +arr[3]) #sum of elements of array


# In[22]:


arr = np.array([[1,2], [3,4]])
print (arr[1,0])


# In[23]:


arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print (arr[1,2-1])


# In[34]:


#array slicing
arr = np.array([1,2,3,4,5,6,7])
print (arr[1:5])
print (arr[4:])
print (arr[:3])
print (arr[-3:-1])
print (arr[1:5:2]) #return every other element
print (arr[::2])


# In[35]:


#Check the data type of array
arr = np.array([1,2,3,4,5])
print (arr.dtype)


# In[36]:


arr = np.array(['apple','banana','mango'])
print (arr.dtype)


# In[37]:


#creating arrays with defined data type
arr = np.array([1,2,3,4,5], dtype ='S') #note* A non integer string like 'a','b' can not converted into integer(will rise an error)
print (arr)
print (arr.dtype)


# In[41]:


#creating an array with data type 4 bytes integer
arr = np.array([1,2,3,4],dtype = 'i4')
print (arr)
print(arr.dtype)


# In[42]:


#Change data type from float to integer
arr = np.array([1.1, 2.2, 3.2, 4.3])
newarr = arr.astype('i') #astype() is use to copy of the array, and allows you to specify data types as a parameter
print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)


# In[45]:


#From integer to boolean
arr = np.array([1,0,3,4])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


# In[46]:


#copy 
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 32
print (arr)
print (x)


# In[47]:


#view
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[2] = 19 #change in original array
print(arr)
print(x)


# In[48]:


#make changes in the view()
arr = np.array([1,2,3,4,5])
x = arr.view()
x[2] = 12 
print(arr)
print(x)


# In[49]:


arr = np.array([1,2,3,4])
x = arr.copy()
y = arr.view()
print(x.base) #The copy return None
print(y.base) #The view return the original array


# In[50]:


#print shape of 2-d array
arr = np.array([[1,2,3], [4,5,6]])
print(arr.shape)


# In[51]:


arr = np.array([1,2,3,4], ndmin = 5)
print (arr)
print ('Shape of array: ', arr.shape)


# In[54]:


#Reshaping of the array
#Convert 1-D array into 2-D array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)


# In[55]:


#Convert 1-D array into 3-D array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)


# In[57]:


#check returned array is view or copy
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base) #we will get original array it means it is a view


# In[60]:


#Flattening the arrays -> means convert multidimensional arrays into 1-D arrays
arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1)
print (arr)
print ('------------------')
print ('After reshape: ' ,newarr)


# In[63]:


#Array iterating
arr = np.array([1,2,3,4])

for x in arr:
    print(x)


# In[64]:


#iterating 2-D array
#If we iterate on a n-D array it will go through n-1th dimension one by one
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)


# In[66]:


#iterate of each scalar element of the 2-D array
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print (y)


# In[72]:


#Join two arrays using Concatenate() function
#concatenate() function is used to join the sequence of arrays along with an existing axis.
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.concatenate((arr1,arr2))
print(arr)


# In[68]:


#join two 2-D arrays using concatenate() function
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2),axis = 1)
print(arr)


# In[93]:


#join two arrays using stack() function
#stack() function is used to join a sequence along with new axis
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.stack((arr1,arr2),axis=1) #we can also use hstack()
print(arr)


# In[75]:


#splitting array 
#array_split is use for splitting arrays into the number of split we want
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,2)
print(newarr)


# In[76]:


#if the array has less element than required, it will adjust from end accordingly
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,4)
print(newarr)


# In[77]:


arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[82]:


#splitting 2-D array
arr = np.array([[1,2,],[3,4],[5,6],[7,8]])
newarr = np.array_split(arr,2)
print(newarr[0])
print(newarr[1])


# In[83]:


#split 2d arrays into 2 2d arrays along with rows
arr = np.array([[1,2,],[3,4],[5,6],[7,8]])
newarr = np.array_split(arr,2,axis=1)
print(newarr[0])
print(newarr[1])


# In[86]:


#split 2d arrays into 2 2d arrays along with rows
#we can use hsplit() method to split arrays along rows without given axis
arr = np.array([[1,2,],[3,4],[5,6],[7,8]])
newarr = np.hsplit(arr,2)
print(newarr)


# In[94]:


#Search array's elements using where method
arr = np.array([1,2,3,4,5,6,4,4])
x = np.where(arr == 4)
print(x) #it will return index where 


# In[96]:


#Finde the index where the values are odd
arr = np.array([1,2,3,4,5,6,7,8,9,10,11])
x = np.where(arr%2 == 1)
print(x)


# In[101]:


#searchsorted() is use to print the index where the array can be insert
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,5)
print(x) #it will print index


# In[99]:


#find the indexes where the value 7 should be inserted , starting from the right
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7,side ='right')
print(x) #it will print index


# In[100]:


arr = np.array([1,3, 5, 7, 9])
x = np.searchsorted(arr,[2,4,6,9])
print (x)


# In[103]:


#sort the array
arr = np.array([0, 12, 3 , 7, 14])
print(np.sort(arr))


# In[104]:


arr = np.array([0, 12, 3 , 7, 14])
x = np.sort(arr)
print(x.base) #sort use copy method


# In[105]:


arr = np.array(['apple','mango','banana','jackfruit'])
print(np.sort(arr))


# In[107]:


arr= np.array([True,False,True])
print(np.sort(arr))


# In[108]:


#sorting 2-D arrays
arr = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))


# In[109]:


#create an array from the element on index 0 and 2
arr = np.array([41,42,43,44])
x = [True, False, True, False]
newarr = arr[x]
print (newarr) 
#it will return [41,43] because the new array contain only the values where the filter array had the value True.


# In[114]:


# create a filter array thet will return only the values higher than 35
arr = np.array([30,32,35,37,39,29,42])
filter_arr = []
for element in arr:
    if element > 35:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# In[117]:


#crate a filter array that will return only even element
arr = np.array([1,2,3,4,5,6,7,8,9,10])
filter_arr = []
for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# In[118]:


#creating filter directly from array
arr = np.array([30,32,35,37,39,29,42])
filter_arr = arr > 35
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# In[ ]:




