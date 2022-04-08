num = int(input())
a_set = set()
b_set = set()

for i in range(num):
	a, b = map(int, input().split())
	a_set.add(a)
	b_set.add(b)

if min(b_set) < max(a_set):
	print('edward is right')
else:
	print('gunilla has a point')
