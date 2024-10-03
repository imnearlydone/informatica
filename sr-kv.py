#6
import numpy as np
x = list(map(float,input().split()))
y = list(map(float,input().split()))
x = np.array(x)
y = np.array(y)
a = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x**2) - np.mean(x)**2)
b = np.mean(y) - a*np.mean(x)
print(round(a,3),' ',round(b,3))