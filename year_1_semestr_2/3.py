A = []
A_t = [[0] * N for i in range(len(A))]
for i in range(len(A)):
    for j in range(len(A)):
        A_t[j][i] = A[i][j]
print(A)