import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
A=pd.read_csv('Admission_Predict.csv');
x=A.iloc[:,1:2].values
y=A.iloc[:,8].values

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=5)
x_poly=poly_reg.fit_transform(x)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y) 

x_grid=np.arange(min(x),max(x),0.1)
x_grid=x_grid.reshape((len(x_grid)),1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,lin_reg2.predict(poly_reg.fit_transform(x_grid)),color='blue')
plt.title('(polynomial regression)')
plt.xlabel('Parameters(Gre)')
plt.ylabel('Chance of getting admission')
plt.show()