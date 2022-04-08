word = input()
rhymes = set()

for i in range(int(input())):
	word_list = input().split()
	for word2 in word_list:
		if word2 == word[-1:-(len(word2)+1):-1][::-1]:
			rhymes |= set(word_list)
			break

for i in range(int(input())):
	last_word = input().split()[-1]
	for rhyme in rhymes:
		if rhyme == last_word[-1:-(len(rhyme)+1):-1][::-1]:
			print('YES')
			break
	else:
		print('NO')
