total = int(input())

for set_number in range(total):
	j, n = input().split()
	j = int(j)
	n = int(n)

	positive = 0
	odd = 0
	even = 0

	for i in range(1, n+1):
		positive += i
		if i % 2 == 0:
			even += i
		else:
			odd += i

	for i in range(n+1, n*2+1):
		if i % 2 == 0:
			even += i
		else:
			odd += i

	print(j, positive, odd, even)
