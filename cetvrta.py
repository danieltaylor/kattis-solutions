x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4 = x1 ^ x2 ^ x3
y4 = y1 ^ y2 ^ y3
print(x4, y4)
