schools = set()

for n in range(int(input())):
	school, team = input().split()
	if len(schools) < 12 and school not in schools:
		schools.add(school)
		print(school, team)
