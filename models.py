import pandas as pd #for DataExploration
import seaborn as sns #for Data Visualization
import matplotlib.pyplot as plt #for Data Visualization
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split



df=pd.read_csv("D:\Python\ml_app\mileage_dataset.csv")# loading the data(csv file) as Pandas DataFrame.


#Independent Features
X=df.drop(['mpg','unamed'],axis=1)
Y=df['mpg']#Dependent Feature
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)#30% testing and 70%training

#model object creation
model=RandomForestRegressor(n_estimators=25,criterion="absolute_error")
model.fit(x_train,y_train)#model training

def predict(df):
    return model.predict(df)
