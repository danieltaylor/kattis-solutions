num = int(input())
count = 0
for i in range(num):
	line = input()
	if 'CD' not in line:
		 count += 1
print(count)
