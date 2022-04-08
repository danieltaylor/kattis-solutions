line = input()
a = 0
b = 0
win_by_two = False

for i in range(0, len(line), 2):
	if line[i] == 'A':
		a += int(line[i + 1])
	else:
		b += int(line[i + 1])

	if a == b == 10:
		win_by_two = True

	if not win_by_two:
		if a >= 11:
			print('A')
		elif b >= 11:
			print('B')
	else:
		if a - 2 >= b:
			print('A')
		elif b - 2 >= a:
			print('B')
