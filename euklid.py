#3
a1 = int(input())
b1 = int(input())
def nod(a, b):
    if a == 0:
        return (0, 1, b)
    else:
        x, y, d = nod(b % a, a)
    return (y - (b // a) * x, x, d)
print(nod(a1, b1))
