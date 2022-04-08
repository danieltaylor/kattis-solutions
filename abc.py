vals = dict()
vals['A'], vals['B'], vals['C'] = sorted(map(int, input().split()))
order = input()
print(vals[order[0]], vals[order[1]], vals[order[2]])
