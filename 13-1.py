with open('13-in', 'r') as f:
	lines = f.read().strip().split('\n')

	carts = []

	for j in range(len(lines)):
		for i in range(len(lines[j])):
			if lines[j][i] == '^' or lines[j][i] == 'v':
				lines[j] = lines[j][:i] + '|' + lines[j][i+1:]
				carts.append((i,j))
			elif lines[j][i] == '<' or lines[j][i] == '>':
				lines[j] = lines[j][:i] + '-' + lines[j][i+1:]
				carts.append((i,j))

	cartd = [0]*len(carts)

	# carts need a direction stored as well as a direction to turn at an intersection

	for cart in carts:
		if lines[j]