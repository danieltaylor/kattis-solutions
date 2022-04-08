def bin_search(arr, val):
	mid = int(len(arr) / 2)
	if val == arr[mid]:
		return val
	elif val > arr[mid]:
		return bin_search(arr[mid + 1:], val)
	else:
		if len(arr) == 1:
			return arr[0]
		elif val > arr[mid - 1] :
			return arr[mid]
		else:
			return bin_search(arr[0:mid], val)

n, m = map(int, input().split())
sizes = [0 for _ in range(n)]
colors = [0 for _ in range(m)]
quick_check = {}

for i in range(n):
	sizes[i] = int(input())
	quick_check[sizes[i]] = sizes[i]
sizes.sort()

for i in range(m):
	colors[i] = int(input())

diff = 0

for val in colors:
	if val in quick_check:
		can = quick_check[val]
	else:
		can = bin_search(sizes, val)
		quick_check[val] = can
	diff += can - val

print(diff)
