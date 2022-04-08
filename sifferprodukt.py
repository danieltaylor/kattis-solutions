value = input()
product = 1

while True:
	for char in value:
		if char != '0':
			product *= int(char)
	if product >= 1 and product <= 9:
		print(product)
		break
	else:
		value = str(product)
		product = 1
