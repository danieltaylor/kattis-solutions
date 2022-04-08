h, w, n = map(int, input().split())
bricks = input().split()

curr_h = 0
curr_w = 0
success = False
for i in range(n):
	curr_w += int(bricks[i])
	if curr_w < w:
		continue
	elif curr_w > w:
		break
	else:
		curr_h += 1
		if curr_h == h:
			success = True
			break
		curr_w = 0

if success:
	print('YES')
else:
	print('NO')
