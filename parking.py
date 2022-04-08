from collections import defaultdict

a, b, c = map(int, input().split())

num_trucks = defaultdict(int)
for i in range(3):
	start, end = map(int, input().split())
	for j in range(start, end):
		num_trucks[j] += 1

total = 0
for time in num_trucks:
	if num_trucks[time] == 1:
		total += a
	elif num_trucks[time] == 2:
		total += b*2
	else:
		total += c*3

print(total)
