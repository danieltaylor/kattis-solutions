from collections import defaultdict

solved = 0
total_time = 0
penalties = defaultdict(int)

line = input()
while line != '-1':
	time, problem, correct = line.split()
	if correct == 'right':
		solved += 1
		total_time += int(time)
		total_time += penalties[problem]
	else:
		penalties[problem] += 20
	line = input()

print(solved, total_time)
