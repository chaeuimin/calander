#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
df = pd.read_csv("FIFA_train.csv")
submission = pd.read_csv('submission.csv')
data_test=pd.read_csv('FIFA_test.csv')
dataset = df.values
dataset
#df['reputation']
df


# In[2]:


df.loc[df["contract_until"]=="Jun 30, 2019","contract_until"] = 2019.5
df.loc[df["contract_until"]=="Dec 31, 2018","contract_until"] = 2019
df.loc[df["contract_until"]=="May 31, 2019","contract_until"] = 2019.5
df.loc[df["contract_until"]=="Jan 31, 2019","contract_until"] = 2018
df.loc[df["contract_until"]=="Jun 30, 2020","contract_until"] = 2020.5
df.loc[df["contract_until"]=="Jan 1, 2019","contract_until"] = 2018
df.loc[df["contract_until"]=="May 31, 2020","contract_until"] = 2020.5
df.loc[df["contract_until"]=="Jan 12, 2019","contract_until"] = 2018
# "2019", 2019를 하나로 묶어주기 위한 타입 변화
df["contract_until"] = df["contract_until"].astype(float)


# In[3]:


df['contract_until']
df.info()


# In[4]:


data = df.iloc[:,4]-2017
data= pd.DataFrame(data)
df.iloc[:,4]= data
df


# In[5]:


import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
dataset = df.values
cnte = df.iloc[:,3]
e = LabelEncoder()
e.fit(cnte)
Y = e.transform(cnte)


po = df.iloc[:,5]
e.fit(po)
Y1= e.transform(po)

fo = df.iloc[:,6]
e.fit(fo)
Y2= e.transform(fo)



Y= pd.DataFrame(Y)
Y1= pd.DataFrame(Y1)
Y2= pd.DataFrame(Y2)
df.iloc[:,3]= Y
df.iloc[:,5]= Y1
df.iloc[:,6]= Y2
df


# In[6]:


df = df.drop(columns = ['name','id', 'continent', 'prefer_foot',])
df


# In[14]:


df.to_csv("EDAtrain")


# In[7]:


data_test = data_test.drop(columns = ['name','id', 'continent', 'prefer_foot'])
data_test


# In[8]:


data_test.loc[data_test["contract_until"]=="Jun 30, 2019","contract_until"] = 2019.5
data_test.loc[data_test["contract_until"]=="Dec 31, 2018","contract_until"] = 2019
data_test.loc[data_test["contract_until"]=="May 31, 2019","contract_until"] = 2019.5
data_test.loc[data_test["contract_until"]=="Jan 31, 2019","contract_until"] = 2018
data_test.loc[data_test["contract_until"]=="Jun 30, 2020","contract_until"] = 2020.5
data_test.loc[data_test["contract_until"]=="Jan 1, 2019","contract_until"] = 2018
data_test.loc[data_test["contract_until"]=="May 31, 2020","contract_until"] = 2020.5
data_test.loc[data_test["contract_until"]=="Jun 1, 2019","contract_until"] = 2019.5
data_test.loc[data_test["contract_until"]=="Dec 31, 2019","contract_until"] = 2020

data_test["contract_until"] = data_test["contract_until"].astype(float)


# In[9]:


data_t = data_test.iloc[:,1]-2017
data_t = pd.DataFrame(data_t)
data_test.iloc[:,1]= data_t
data_test


# In[10]:


dataset_test = data_test.values
cnte = data_test.iloc[:,2]
e = LabelEncoder()
e.fit(cnte)
Y = e.transform(cnte)
Y= pd.DataFrame(Y)
data_test.iloc[:,2]= Y
data_test


# In[13]:


data_test.to_csv("EDAtest")

