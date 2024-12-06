n = int(input())
wins_am = int(input())
D = {}
for i in range(n):
    s = input()
    if s in D:
        D[s] += 1
    else:
        D[s] = 1
i = 1
print(D)
A = list(D.keys())
B = list(D.values())
for i in range(1, wins_am + 1):
    for j in range(len(B)):
        if B[j] == max(B):
            print(A[j], ' - ', B[j])
            A.pop(j)
            B.pop(j)
            break
    i += 1