capacity, loss, miles = map(float, input().split())
efficiency = dict()

for i in range(6):
	speed, gallons_per_hour = map(float, input().split())
	efficiency[speed] = gallons_per_hour

for speed in range(80, 54, -5):
	hours = miles / speed
	gallons_lost = (loss * hours) + (miles / efficiency[speed])
	if gallons_lost < capacity / 2:
		print('YES', speed)
		break
else:
	print('NO')
