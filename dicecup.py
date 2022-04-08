n, m = map(int, input().split())

if n == m:
	print(n + 1)
else:
	for i in range(min(n, m) + 1, max(n, m) + 2):
		print(i)
