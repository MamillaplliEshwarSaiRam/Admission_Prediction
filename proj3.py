import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A=pd.read_csv('Admission_Predict.csv');
x=A.iloc[:,1:2].values
y=A.iloc[:,8].values

A=A.sort_values(by='Chance of Admit ')
objects=list(range(0,10))
performance=A['Chance of Admit '][:10]
y_pos=np.arange(len(objects))
colors=['blue','red','purple','grey','brown']
patches=plt.barh(y_pos,performance,align='center',color=colors)
plt.yticks(y_pos,objects)
plt.title('Students with highest chance of admission')
plt.xlabel('Gre ')
plt.legend(patches,objects,loc='best')
plt.show()