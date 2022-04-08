from collections import deque

stack = deque()

n = int(input())

for _ in range(n):
	stack.append(input())

for _ in range(n):
	print(stack.pop())
