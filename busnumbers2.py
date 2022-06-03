def main():
	m = int(input())

	cubes = dict()
	one_way = set()
	two_ways = set()
	max_val = 0

	for hi in range(int(m**(1./3)), 1, -1):
		for lo in range(0, hi):
			if lo in cubes:
				lo_cubed = cubes[lo]
			else:
				lo_cubed = lo**3
				cubes[lo] = lo_cubed
			sum = hi**3 + lo_cubed
			if sum > m:
				break
			if sum in two_ways:
				continue
			if sum <= m:
				if sum in one_way:
					one_way.remove(sum)
					two_ways.add(sum)
					if sum == m:
						return m
					elif sum > max_val:
						max_val = sum
				else:
					one_way.add(sum)

	return max_val


max_val = main()
if max_val:
	print(max_val)
else:
	print('none')
