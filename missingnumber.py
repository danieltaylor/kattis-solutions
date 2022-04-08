num = int(input())
line = input()

compare = ''

for i in range(1, num + 1):
	compare += str(i)
	if line[:len(compare)] != compare:
		print(i)
		break
