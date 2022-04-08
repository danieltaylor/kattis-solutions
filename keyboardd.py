from collections import Counter

line1 = Counter(input())
line2 = Counter(input())

print(''.join(list(line2 - line1)))
