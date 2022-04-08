left_top = 8
right_top = 8
left_bot = 8
right_bot = 8

n = int(input())
for _ in range(n):
	line = input()
	if line[0].isdigit():
		if 'b' in line:
			right_top = 0
			right_bot = 0
		else:
			if '+' in line:
				right_top -= 1
			else:
				right_bot -= 1
	else:
		if 'b' in line:
			left_top = 0
			left_bot = 0
		else:
			if '+' in line:
				left_top -= 1
			else:
				left_bot -= 1

if left_top > 0 and left_bot > 0:
	print(0)
elif right_top > 0 and right_bot > 0:
	print(1)
else:
	print(2)
