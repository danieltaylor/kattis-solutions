num = int(input())
tb = 0
lr = 0

for i in range(num):
	sword = input()
	if sword[0] == '0':
		tb += 1
	if sword[1] == '0':
		tb += 1
	if sword[2] == '0':
		lr += 1
	if sword[3] == '0':
		lr += 1

min = min(tb, lr)
if min % 2 != 0:
	min -= 1

print(int(min/2), tb - min, lr - min)
