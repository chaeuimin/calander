#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("EDAtrain.csv")
data_test=pd.read_csv('EDAtest.csv', encoding='utf-8')


# In[3]:


df = df.iloc[:,1:]
df


# In[4]:


data_test = data_test.iloc[:,1:]
data_test


# In[5]:


from sklearn.ensemble import GradientBoostingRegressor
train_x = df.drop(columns = ['value'])
train_y = df['value']
gb = GradientBoostingRegressor(random_state=1)
gb.fit(train_x, train_y)


# In[6]:


from sklearn.model_selection import train_test_split
train_x=train_x.astype(float)
train_y=train_y
X_train, X_test,Y_train, Y_test = train_test_split(train_x,train_y,test_size=0.3,random_state=0)


# In[7]:


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 함수정리
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs(y_true-y_pred) / y_true) * 100

def norm_mean_absolute_error(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)/np.mean(np.abs(y_true))

def regression_scores(y_true,y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    nmae = norm_mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {'mse':np.round(mse,3), 'rmse':np.round(rmse,3), 'mae':np.round(mae,3), 'nmae':np.round(nmae,3), 'mape':np.round(mape,3), 'r2':np.round(r2,3) }  


# In[8]:


from sklearn.ensemble import RandomForestRegressor
import numpy as np
y_pred = gb.predict(X_test)
score = regression_scores(y_pred, Y_test)
score


# In[9]:


Y_test


# In[11]:


from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(train_x,train_y,test_size=0.3,random_state=0)
Y_prediction = gb.predict(X_test).flatten()


# In[12]:


import math
for i in range(10):
    prediction = Y_prediction[i]
    print( "예상가격: {:.6f}".format(prediction))


# ## class를 log_value로 모델링

# In[13]:


df["log_value"] = np.log(df["value"])


# In[18]:


from sklearn.ensemble import RandomForestRegressor
train_x = df.drop(columns = ['value','log_value'])
train_y = df['log_value']
gb = GradientBoostingRegressor(random_state=1)
gb.fit(train_x, train_y)


# In[19]:


from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(train_x,train_y,test_size=0.3,random_state=0)
Y_prediction = gb.predict(X_test).flatten()
Y_test


# In[20]:


for i in range(10):
    prediction = Y_prediction[i]
    print( "예상가격: {:.6f}".format(prediction))


# In[21]:


from sklearn.ensemble import RandomForestRegressor
import numpy as np
y_pred = gb.predict(X_test)
score = regression_scores(y_pred, Y_test)
score


# In[ ]:




