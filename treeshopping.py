from collections import Counter

n, k = map(int, input().split())
trees = list(map(int, input().split()))

section = Counter(trees[0:k])

min_diff = max(section) - min(section)

for i in range(1, n - k + 1):
	if section[trees[i - 1]] == 1:
		del section[trees[i - 1]]
	else:
		section[trees[i - 1]] -= 1
	section[trees[i + k - 1]] += 1

	diff = max(section) - min(section)


	if diff < min_diff:
		min_diff = diff

print(min_diff)
