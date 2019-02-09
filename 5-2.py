def react(poly):
	i = len(poly) - 2

	while i >= 0:
		if abs(ord(poly[i]) - ord(poly[i+1])) == 32:
			del poly[i+1]
			del poly[i]
			if i == len(poly):
				i -= 1
		i -= 1

	return len(poly)

with open('5-in', 'r') as f:
	poly = list(f.read().strip())

	minp = len(poly)

	for i in range(ord('a'), ord('z')+1):
		p = react([c for c in poly if ord(c) != i and ord(c) != i-32])
		if p < minp:
			minp = p

	print(minp)
