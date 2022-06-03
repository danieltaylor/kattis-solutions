n = int(input())

prev = tuple(map(int, input().split()))
max_speed = 0

for i in range(n-1):
	curr = tuple(map(int, input().split()))
	speed = (curr[1] - prev[1]) / (curr[0] - prev[0])
	if speed > max_speed:
		max_speed = speed
	prev = curr

print(int(max_speed))
