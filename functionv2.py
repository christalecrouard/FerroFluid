from ctypes import sizeof
import pandas as pd
import csv
import numpy as np

from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
                

df = pd.read_csv("data.csv") 
X = df[['height']]

y = df[['mag_field']]


angle=  df[['angle']]
module = df[['module']]

from sklearn import linear_model 

regr = linear_model.LinearRegression()

arr1=[]
arr2=[]
arr3=[]
ary1=[]

X = X.to_numpy()
angle = angle.to_numpy()
module = module.to_numpy()
pred = y.to_numpy()

for i in range(359):
    a1 = ((X[i][0][1:-1].split(','))[0])
    a2 = ((angle[i][0][1:-1].split(','))[0])
    a3 = ((module[i][0][1:-1].split(','))[0])

    y1 = ((pred[i][0]))
    if a1 == '' or a2 == '' or a3 == '' or y1 == '':
        a1 = 0
        a2 = 0
        a3 = 0
        y1 = 0
    arr2.append(float(a2))
    arr1.append(float(a1))
    arr3.append(float(a3))
    ary1.append(float(y1))

new_X = pd.DataFrame(list(zip(arr1, arr2, arr3)),columns =['height', 'angle', 'module'])

plt.title("Magn") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(arr3,ary1) 
plt.show()

X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.30, random_state=40)
print("training input : ",X_train.shape); print("testing input : ",X_test.shape)

dtree = DecisionTreeRegressor(max_depth=1500, min_samples_leaf=0.13, random_state=3)
dtree.fit(X_train, y_train)

pred_train_tree= dtree.predict(X_train)
print("rmse training : ", np.sqrt(mean_squared_error(y_train,pred_train_tree)))
print("r squared training : ", r2_score(y_train, pred_train_tree))

pred_test_tree= dtree.predict(X_test)
print("rmse testing : ", np.sqrt(mean_squared_error(y_test,pred_test_tree))) 
print("r squared testing : ", r2_score(y_test, pred_test_tree))

#Fit the regression tree 'dtree1' and 'dtree2' 
dtree1 = DecisionTreeRegressor(max_depth=2)
dtree2 = DecisionTreeRegressor(max_depth=5)
dtree1.fit(X_train, y_train)
dtree2.fit(X_train, y_train)

#Predict on training data
tr1 = dtree1.predict(X_train)
tr2 = dtree2.predict(X_train) 

#Predict on testing data
y1 = dtree1.predict(X_test)
y2 = dtree2.predict(X_test)

# Print RMSE and R-squared value for regression tree 'dtree1' on training data
print("rmse training tree 1 : ", np.sqrt(mean_squared_error(y_train,tr1))) 
print("r squared training tree 1 : ", r2_score(y_train, tr1))

# Print RMSE and R-squared value for regression tree 'dtree1' on testing data
print("rmse testing tree 1 : ", np.sqrt(mean_squared_error(y_test,y1))) 
print("r squared testing tree 1 : ", r2_score(y_test, y1))

# Print RMSE and R-squared value for regression tree 'dtree2' on training data
print("rmse training tree 2 : ", np.sqrt(mean_squared_error(y_train,tr2))) 
print("r squared training tree 2 : ", r2_score(y_train, tr2))

# Print RMSE and R-squared value for regression tree 'dtree2' on testing data
print("rmse testing tree 2 : ", np.sqrt(mean_squared_error(y_test,y2))) 
print("r squared testing tree 2 : ", r2_score(y_test, y2)) 

print("\n")

#RF model

model_rf = RandomForestRegressor(n_estimators=5000, oob_score=True, random_state=100)
model_rf.fit(X_train, y_train) 
pred_train_rf= model_rf.predict(X_train)
print(np.sqrt(mean_squared_error(y_train,pred_train_rf)))
print(r2_score(y_train, pred_train_rf))

pred_test_rf = model_rf.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,pred_test_rf)))
print(r2_score(y_test, pred_test_rf))

print(model_rf.predict([[170, 1.200472897092122, 182.36227680087788]]))

#60% test r square score