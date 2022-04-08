r, c = input().split()
while r != '0':
	lines = int(r)
	chars = int(c)

	cols = ['' for i in range(chars)]
	rows = [0 for i in range(lines)]

	for i in range(lines):
		rows[i] = input()

	for i in range(lines):
		for j in range(chars):
			cols[j] += rows[i][j]

	cols.sort(key=str.lower)

	for i in range(lines):
		word = ''
		for j in range(chars):
			word += cols[j][i]
		print(word)
	r, c = input().split()
	if r != '0':
		print()
