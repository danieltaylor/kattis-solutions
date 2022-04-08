codes = {
	'a': '2',
	'b': '22',
	'c': '222',
	'd': '3',
	'e': '33',
	'f': '333',
	'g': '4',
	'h': '44',
	'i': '444',
	'j': '5',
	'k': '55',
	'l': '555',
	'm': '6',
	'n': '66',
	'o': '666',
	'p': '7',
	'q': '77',
	'r': '777',
	's': '7777',
	't': '8',
	'u': '88',
	'v': '888',
	'w': '9',
	'x': '99',
	'y': '999',
	'z': '9999',
	' ': '0'
}

num = int(input())

for i in range(num):
	text = input()
	translation = ''

	prev_code = ' '

	for c in text:
		curr_code = codes[c]
		if curr_code[0] == prev_code[0]:
			translation += ' ' + curr_code
		else:
			translation += curr_code
		prev_code = curr_code

	print('Case #' + str(i + 1) + ': ' + translation)
