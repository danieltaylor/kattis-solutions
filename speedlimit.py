while True:
	n = int(input())
	if n == -1:
		break
	total = 0
	prev = 0
	for i in range(n):
		a, b = map(int, input().split())
		total += a * (b-prev)
		prev = b
	print(total, 'miles')
