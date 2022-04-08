import sys

definitions = dict()

for line in sys.stdin:
	line = str(line).split()
	if line[0] == 'define':
		definitions[line[2]] = int(line[1])
	elif line[0] == 'eval':
		var1 = line[1]
		operator = line[2]
		var2 = line[3]
		if var1 in definitions and var2 in definitions:
			val1 = definitions[var1]
			val2 = definitions[var2]
			if operator == '<':
				print(str(val1 < val2).lower())
			elif operator == '>':
				print(str(val1 > val2).lower())
			elif operator == '=':
				print(str(val1 == val2).lower())
		else:
			print('undefined')
