N = int(input())
edge_list = [[3, 5], [1, 4], [8,6], [6, 8], [1, 2]]
A = [[0] * N for i in range(N)]
for i in range(len(edge_list)):
    A[edge_list[i][0] - 1][edge_list[i][0] - 1] = 1
for j in A:
    print(" ".join(map(str, j)))