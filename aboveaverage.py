from statistics import mean

n = int(input())

for _ in range(n):
	values = list(map(int, input().split()))
	average = mean(values[1:])

	above = 0
	for i in range(1, values[0] + 1):
		if values[i] > average:
			above += 1

	print(f'{above/values[0] * 100:.3f}%')
