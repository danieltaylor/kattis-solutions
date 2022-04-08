n = int(input())
total = 0

a, b = map(float, input().split())

for i in range(1, n):
	c, d = map(float, input().split())
	total += (d + b)/2 * (c-a)
	a, b = c, d

print(total/1000)
