#5
import numpy as np
n = int(input())
n1 = n
m = int(input())
m1 = m
a = np.zeros((n,m),int)
c = 1
i, j = 0, 0
while (i < n and j < m):
        for p in range(j, m):
            a[i][p] = c
            c += 1
        i += 1
        for p in range(i, n):
            a[p][m - 1] = c
            c += 1
        m -= 1
        if (j < m):
            for p in range(m - 1, j - 1, -1):
                a[n - 1][p] = c
                c += 1
            n -= 1
        if (i < n):
            for p in range(n - 1, i - 1, -1):
                a[p][j] = c
                c += 1
            j += 1
#print(a)
for i in range(n1):
    for j in range(m1):
        a[i][j] = (i+1) * a[i][j]
print(a)
