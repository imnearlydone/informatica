n = int(input())
a = []
i = 2

def simple(m):
    p = 0
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            p = 1
            break
    if p == 0:
        return True
    else:
        return False

while n > 1:
    if n % i == 0 and simple(i) == True:
        a.append(i)
        n = n // i
    else:
        i+=1
for i in range(len(a)):
    if i == 0:
        print(a[i],'^',a.count(a[i]),end=', ')
    elif a[i] == a[i-1]:
        continue
    else:
        print(a[i],'^',a.count(a[i]),end=', ')
