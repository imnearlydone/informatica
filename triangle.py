#4
size = int(input())
sym = input()
def triangle(h,depth = 1, symbol = sym):
    if h % 2 != 0 and depth == h // 2 + 1:
        print(symbol * depth)
        return
    if h % 2 == 0 and depth == h // 2:
        print(symbol * depth)
        print(symbol * depth)
        return
    print(symbol * depth)
    triangle(h, depth = depth + 1)
    print(symbol * depth)
triangle(size,1,sym)