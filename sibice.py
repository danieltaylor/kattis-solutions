from math import sqrt

n, w, h = map(int, input().split())

for _ in range(n):
	l = int(input())
	if l <= sqrt(w**2 + h**2):
		print('DA')
	else:
		print('NE')
