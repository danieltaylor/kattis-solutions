n = int(input())
mult = None

for i in range(n):
	num = int(input())
	if mult == None:
		mult = num
	else:
		if num % mult == 0:
			print(num)
			mult = None
