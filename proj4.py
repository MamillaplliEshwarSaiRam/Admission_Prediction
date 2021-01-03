import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A=pd.read_csv('Admission_Predict.csv');
A=A.sort_values(by='Chance of Admit ',ascending=False)
labels=[]
ct=0
for i in A:
    if(ct!=0 and ct<3 and ct!=A.shape[1]-1):
        labels.append(i)
    ct+=1

print(A.loc[0]['GRE'])
sizes=[]
for i in range(1,3):
    sizes.append(A.loc[0][i])


colors=['brown','blue','pink','silver','red','purple']
explode=[0.1,0.2]
plt.pie(sizes,labels=labels,colors=colors,autopct="%1.3f",explode=explode)
plt.axis('equal')
plt.show()