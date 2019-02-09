with open('5-in', 'r') as f:
	poly = list(f.read().strip())

	i = len(poly) - 2

	while i >= 0:
		if abs(ord(poly[i]) - ord(poly[i+1])) == 32:
			del poly[i+1]
			del poly[i]
			if i == len(poly):
				i -= 1
		i -= 1

	print(len(poly))
