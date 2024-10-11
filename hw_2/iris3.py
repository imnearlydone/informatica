import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
data = pd.read_csv("iris_data.csv")
a = 0
b = 0
c = 0

'''x1 = data["Species"]
for i in range(len(x1)):
    if x1[i] == 'Iris-setosa':
        a+=1
    elif x1[i] == 'Iris-versicolor':
        b+=1
    elif x1[i] == 'Iris-virginica':
        c+=1
plt.pie([a/(a+b+c), b/(a+b+c), c/(a+b+c)], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
plt.title('Types of iris')'''

x1 = data["PetalLengthCm"]
for i in range(len(x1)):
    if x1[i] <= 1.2:
        a+=1
    elif x1[i] <= 1.5:
        b+=1
    else:
        c+=1
plt.pie([a/(a+b+c), b/(a+b+c), c/(a+b+c)], labels = ['PetalLengthCm <= 1.2','1.2 < PetalLengthCm <= 1.5','PetalLengthCm > 1.5'])
plt.title('Lengths of petals')
plt.show()
#закомментированная часть отвечает за построение первой диаграммы