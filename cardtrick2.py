from collections import deque

for _ in range(int(input())):
	n = int(input())
	deck = deque()
	for i in range(n, 0, -1):
		deck.appendleft(str(i))
		deck.rotate(i)
	print(' '.join(deck))
