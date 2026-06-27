import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv("../data/raw/Student_Performance.csv")

df["Extracurricular Activities"]=df["Extracurricular Activities"].map({"Yes":1,"No":0})

X=df.drop("Performance Index",axis=1)
y=df["Performance Index"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

joblib.dump(model,"../models/linear_regression.pkl")
print("Model Saved Sucessfully")