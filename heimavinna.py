sets = input().split(';')
num = 0
for set in sets:
	if '-' in set:
		set = set.split('-')
		num += int(set[1]) - int(set[0]) + 1
	else:
		num += 1
print(num)
