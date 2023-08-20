#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Create a simple pandas series from a list
import pandas as pd
a= [1,7,4]
myvar = pd.Series(a)
print(myvar)


# In[3]:


#Return the first value of the series
print(myvar[0])


# In[4]:


#craete your own labels
a = [1,4,6,10,9]
myvar = pd.Series(a,index=["a","b","c","d","e"])
print(myvar)


# In[6]:


#Return the value of d
print(myvar["d"])


# In[7]:


#create a Pandas series from a dictionary
calories ={"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories)
print(myvar)


# In[8]:


#return the series of only day1 and day2
calories ={"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories,index = ["day1","day2"])
print(myvar)


# In[9]:


data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)


# In[10]:


#refer the row index
print(myvar.loc[0])


# In[11]:


#return row 0 and 1
print(myvar.loc[[0,1]])


# In[12]:


data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data,index = ["day1","day2","day3"])
print(myvar)


# In[14]:


#return day2 or locate name index
print(myvar.loc["day2"])


# In[18]:


df = pd.read_csv('Groceries_dataset.csv')
print(df)


# In[19]:


#load csv in to Data Frame
print(df.to_string())


# In[20]:


#Check th enumber of maximum returned rows
print(pd.options.display.max_rows)


# In[24]:


#Increse the maximum number of rows to disply entire Data Frames
pd.options.display.max_rows=9999
df = pd.read_csv('Groceries_dataset.csv')
print(df)


# In[ ]:


#load JSON file into data frame
df = pd.read_json('data.json')
print(df.to_string())


# In[29]:


#Load Python dictionary into data frame

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 


# In[34]:


#print 5 rows from first
df = pd.read_csv('Groceries_dataset.csv')
print(df.head())


# In[33]:


#Print 10 rows from first
df = pd.read_csv('Groceries_dataset.csv')
print(df.head(10))


# In[35]:


#print last 5 rows
print(df.tail())


# In[36]:


#print information about data
print(df.info())


# In[62]:


#Retuen all rows without null values
df = pd.read_csv ('data.csv')
new_df = df.dropna()
print(new_df.to_string())


# In[65]:


#Remove all rows with NULL values
df = pd.read_csv ('Groceries_dataset.csv')
df.dropna(inplace = True)
print(df.to_string())


# In[66]:


#Replace NULL values with the number 000
df.fillna(130, inplace = True)
print(df)


# In[49]:


df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())


# In[51]:


#remove rows with a NULL value in "Date" column
df.dropna(subset=['Date'],inplace = True)
print(df.to_string())


# In[52]:


#set "Member Number" = 3333 in row 5
df.loc[5,'Member_number'] = 3333
print(df.head(10))


# In[53]:


#If the value is higher than 4000 , set it to the 4000
for x in df.index:
    if df.loc[x,"Member_number"] > 4000:
        df.loc [x, "Member_number"] = 4000
print(df.to_string())


# In[55]:


#Rumove rows whole values is 4000:
for x in df.index:
    if df.loc[x,"Member_number"] == 4000:
        df.drop(x,inplace = True)
print(df.to_string())


# In[67]:


#print duplicate values
df = pd.read_csv('Data.csv')
print(df.duplicated())


# In[68]:


#reomve duplicates values
print(df.drop_duplicates(inplace = True))


# In[69]:


#Show the relationship between columans
print(df.corr(numeric_only=True))


# In[70]:


import matplotlib.pyplot as plt
df.plot()
plt.show()


# In[71]:


#Scatter plot of Duration and calories 
df.plot(kind = 'scatter', x = 'Duration' , y = 'Calories')
plt.show()


# In[72]:


df.plot(kind = 'scatter', x = 'Duration' , y = 'Maxpulse')
plt.show()


# In[74]:


#Histogarm
df["Duration"].plot(kind = 'hist')
plt.show()


# In[ ]:




