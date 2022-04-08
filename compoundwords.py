import sys

words = []

for line in sys.stdin:
	words.extend(line.split())

compound_words = set()

for i in range(len(words)):
	for j in range(len(words)):
		if i == j:
			continue
		compound_words.add(words[i] + words[j])

for compound in sorted(compound_words):
	print(compound)
