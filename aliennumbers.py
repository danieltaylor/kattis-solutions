num_cases = int(input())

for case in range(num_cases):
	alien_number, source_language, target_language = input().split()

	source_map = {}
	target_map = {}

	for i in range(len(source_language)):
		source_map[source_language[i]] = i
	for i in range(len(target_language)):
		target_map[i] = target_language[i]

	alien_number_arabic = []
	for c in alien_number:
		alien_number_arabic.append(str(source_map[c]))

	decimal_value = 0
	for i in range(0, len(alien_number_arabic)):
		decimal_value += int(alien_number_arabic[len(alien_number_arabic) - 1 - i]) * (len(source_language)**i)

	target_number_arabic = []
	while decimal_value != 0:
		target_number_arabic.append(decimal_value % (len(target_language)))
		decimal_value = int(decimal_value / len(target_language))

	target_number = ''
	for i in range(len(target_number_arabic)):
		target_number += target_map[target_number_arabic[len(target_number_arabic) - 1 - i]]

	print('Case #' + str(case + 1) + ': ' + target_number)
