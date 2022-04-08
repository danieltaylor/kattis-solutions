import string

line = input()
acr = ''

for char in line:
	if char in string.ascii_uppercase:
		acr += char

print(acr)
