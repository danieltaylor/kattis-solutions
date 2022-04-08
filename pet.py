high_score = 0
winner = 0
for i in range(1, 6):
	score = sum(list(map(int, input().split())))
	if score > high_score:
		high_score = score
		winner = i
print(winner, high_score)
