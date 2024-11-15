import time
from random import randint
import copy
import numpy as np
import matplotlib.pyplot as plt
a = []
x1 = [0]
y1 = [0]
x2 = [0]
y2 = [0]
x3 = [0]
y3 = [0]
k = 1
while k <= 100:  #хотелось существенно больше, для более плавного графика, но время работы и так велико
    for i in range (k):
        a.append(randint(-1000, 1000))

    #пузырек
    a1 = copy.copy(a)
    st_time = time.time()
    for i in range(len(a1)-1):
        for j in range(len(a1) - 1 - i):
            if a1[j] > a1[j + 1]:
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
    en_time = time.time()
    x1.append(k)
    y1.append(en_time - st_time)
    #выбор
    a2 = copy.copy(a)
    st_time = time.time()
    for i in range(len(a) - 1):
        p = i
        j = i + 1
        for j in range(len(a)):
            if a2[j] < a2[p]:
                p = j
                j += 1
        a2[i], a2[p] = a2[p], a2[i]
    en_time = time.time()
    x2.append(k)
    y2.append(en_time - st_time)
    #вставки
    a3 = copy.copy(a)
    st_time = time.time()
    for i in range(1, len(a)):
        j = i - 1
        while j >= 0 and a[i] < a[j]:
            a3[j + 1] = a3[j]
            j -= 1
            a3[j + 1] = i
    en_time = time.time()
    x3.append(k)
    y3.append(en_time - st_time)
    k += 1
print(y1)
print(y2)
print(y3)
#график
plt.figure()
plt.plot(x1, y1, 'red') #пузырек
plt.plot(x2,y2, 'yellow') #выбор
plt.plot(x3,y3,'green') #вставки
plt.legend()
plt.show()



