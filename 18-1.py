def adjacent(c, acres, i, j):
	n = 0
	if acres[j][i-1] == c:
		n += 1
	if acres[j+1][i-1] == c:
		n += 1
	if acres[j-1][i] == c:
		n += 1
	if acres[j-1][i+1] == c:
		n += 1
	if acres[j-1][i-1] == c:
		n += 1
	if acres[j][i+1] == c:
		n += 1
	if acres[j+1][i+1] == c:
		n += 1
	if acres[j+1][i] == c:
		n += 1
	return n

with open('18-in', 'r') as f:
	lines = f.read().strip().split('\n')

	empty = [' ']*(len(lines[0])+2)
	acres = []

	acres.append(empty)
	for line in lines:
		a = []
		a.append(' ')
		a.extend(line)
		a.append(' ')
		acres.append(a)
	acres.append(empty)

	for x in range(10):
		nacres = []

		for j in range(len(acres)):
			n = []

			for i in range(len(acres[0])):
				if acres[j][i] == '.':
					trees = adjacent('|', acres, i, j)
					if trees >= 3:
						n.append('|')
					else:
						n.append('.')
				elif acres[j][i] == '|':
					lumb = adjacent('#', acres, i, j)
					if lumb >= 3:
						n.append('#')
					else:
						n.append('|')
				elif acres[j][i] == '#':
					trees = adjacent('|', acres, i, j)
					lumb = adjacent('#', acres, i, j)
					if trees >= 1 and lumb >= 1:
						n.append('#')
					else:
						n.append('.')
				else:
					n.append(' ')

			nacres.append(n)

		acres = nacres

	t = 0
	l = 0

	for j in range(len(acres)):
		for i in range(len(acres[0])):
			if acres[j][i] == '|':
				t += 1
			elif acres[j][i] == '#':
				l += 1

	print(int(t)*l)
