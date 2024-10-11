import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
data = pd.read_csv("iris_data.csv")
x1 = data["SepalLengthCm"]
y1 = data["SepalWidthCm"]
x2 = data["PetalLengthCm"]
y2 = data["PetalWidthCm"]
a = 'PetalLengthCm'
b ='PetalWidthCm'
plt.xlabel(a)
plt.ylabel(b)
plt.scatter(x2,y2) #так как при использовании "plot", на графике вообще ничего непонятно
plt.show()

#После построения всех 6 зависимостей, закономерности вывести не удалось