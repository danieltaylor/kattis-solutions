num = int(input())

arr = [0 for _ in range(num)]
arr_post = [0 for _ in range(num)]
arr_sq = [0 for _ in range(num)]
arr_sq_pref = [0 for _ in range(num)]

for i in range(num):
	arr[i] = int(input())
	arr_sq[i] = arr[i]**2
	arr_sq_pref[i] = arr_sq[i] + (arr_sq_pref[i - 1] if i > 0 else 0)

for i in range(num-1, -1, -1):
	arr_post[i] = arr[i] + ( 0 if i == num-1 else arr_post[i + 1])

max = 0

for i in range(num-1):
	if arr_sq_pref[i] * arr_post[i+1]> max:
		max = arr_sq_pref[i] * arr_post[i+1]

print(max)
