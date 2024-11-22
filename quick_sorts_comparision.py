import time
from random import randint
import copy
import numpy as np
import matplotlib.pyplot as plt
def merge(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    res += A[i:] + B[j:]
    return res
def merge_sort(b):
    if len(b) < 2:
        return b
    mid = len(b) // 2
    left = b[:mid]
    right = b[mid:]
    return merge(merge_sort(left), merge_sort(right))
def qsort(A, left = 0, right = None):
    if right is None:
        right = len(A) - 1
    if left >= right:
        return
    i = left
    j = right
    pivot = A[left]
    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    qsort(A, left, j)
    qsort(A, i, right)
a = []
x1 = [0]
y1 = [0]
x2 = [0]
y2 = [0]
k = 50
while k <= 500: #работает довольно долго, зато много точек
    for i in range (k):
        a.append(randint(-1000, 1000))
    #merge
    a1 = copy.copy(a)
    st_time = time.time()
    merge_sort(a1)
    en_time = time.time()
    x1.append(k)
    y1.append(en_time - st_time)
    # qsort
    a2 = copy.copy(a)
    st_time = time.time()
    qsort(a2)
    en_time = time.time()
    x2.append(k)
    y2.append(en_time - st_time)
    k += 1
print(y1)
print(y2)
#график
plt.figure()
plt.plot(x1, y1, 'green') #merge
plt.plot(x2, y2, 'red') #qsort
plt.legend()
plt.show()