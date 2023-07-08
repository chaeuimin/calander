#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
df = pd.read_csv("EDAtrain.csv")
data_test=pd.read_csv('EDAtest.csv')


# In[61]:


df = df.iloc[:,1:]
df


# In[62]:


data_test = data_test.iloc[:,1:]
data_test


# ## 가장 기본적인 형태의 AdaBoost

# In[63]:


from sklearn.ensemble import AdaBoostRegressor


# In[64]:


clf = AdaBoostRegressor(n_estimators=10, random_state=0)
train_x = df.drop(columns = ['value'])
train_y = df['value']
clf.fit(train_x, train_y) 


# In[65]:


from sklearn.model_selection import train_test_split
train_x=train_x.astype(float)
train_y=train_y
X_train, X_test,Y_train, Y_test = train_test_split(train_x,train_y,test_size=0.3,random_state=0)


# In[66]:


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 함수정리
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs(y_true-y_pred) / y_true) * 100


def regression_scores(y_true,y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return { 'rmse':np.round(rmse,3) }  


# In[67]:


import numpy as np
y_pred =clf.predict(X_test)
score = regression_scores(y_pred, Y_test)
score


# In[68]:


Y_test


# In[69]:


Y_prediction = clf.predict(X_test).flatten()


# In[70]:


import math
for i in range(10):
    prediction = Y_prediction[i]
    print( "예상가격: {:.6f}".format(prediction))


# ## Decision Tree 기반의 AdaBoost

# In[71]:


from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score


# In[72]:


tree_model = DecisionTreeRegressor(max_depth=5)
declf = AdaBoostRegressor(base_estimator = tree_model, n_estimators=10, random_state=0)
declf.fit(train_x, train_y) 


# In[73]:


y_pred =declf.predict(X_test)
score = regression_scores(y_pred, Y_test)
score


# In[74]:


Y_prediction = declf.predict(X_test).flatten()


# In[75]:


for i in range(10):
    prediction = Y_prediction[i]
    print( "예상가격: {:.6f}".format(prediction))


# ## 추정 횟수를 증가시킨 AdaBoost

# In[76]:


tree_model = DecisionTreeRegressor(max_depth=5)
deadclf = AdaBoostRegressor(base_estimator = tree_model, n_estimators=100, random_state=0)
deadclf.fit(train_x, train_y) 


# In[77]:


y_pred =deadclf.predict(X_test)
score = regression_scores(y_pred, Y_test)
score


# In[78]:


Y_prediction = deadclf.predict(X_test).flatten()


# In[79]:


for i in range(10):
    prediction = Y_prediction[i]
    print( "예상가격: {:.6f}".format(prediction))


# ## 트리의 깊이를 증가시킨 AdaBoost

# In[80]:


tree_model = DecisionTreeRegressor(max_depth=30)
deadsclf = AdaBoostRegressor(base_estimator = tree_model, n_estimators=10, random_state=0)
deadsclf.fit(train_x, train_y) 


# In[81]:


import joblib
joblib.dump(deadsclf, './adboost.pkl')


# In[82]:


y_pred =deadsclf.predict(X_test)
score = regression_scores(y_pred, Y_test)
score


# In[83]:


Y_prediction = deadsclf.predict(X_test).flatten()
for i in range(10):
    prediction = Y_prediction[i]
    print( "예상가격: {:.6f}".format(prediction))


# In[ ]:





# In[ ]:




