from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics #for calculating accuracy
import numpy as np

def home(request):
    return render(request, 'index.html')

def predict(request):
    return render(request, 'predict.html')

def solution(request):
    data = pd.read_csv(r"D:\Dataset\USA_Housing.csv") #set the path of Dataset on your computer
    data = data.drop(['Address'],axis=1)
    x = data.drop('Price',axis=1) #contains all columns except price
    y = data['Price']
    x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.30)
    model = LinearRegression()
    model.fit(x_train, y_train)

    #takes the input values and stores to the given variable
    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    pred = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1)) #converts 1D arr to 2D arr
    pred = round(pred[0])

    price = 'The predicted price of House is $' + str(pred)
    return render(request, 'predict.html',{'result' : price})
