n, m = map(int, input().split())
groups = list(map(int, input().split()))

count = 0
for i in range(0, m):
	count += groups[i]
	if count > n:
		print(m - i)
		break
else:
	print(0)
