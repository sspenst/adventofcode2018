def water_from_spring(x, y):
	water = 0
	still = 0

	while (x, y+1) not in clay and (x, y+1) not in sand and y < maxy:
		y += 1
		sand.add((x, y))
		if y >= miny:
			water += 1

	if y == maxy:
		return water, still, False

	if (x, y+1) in sand:
		x1 = x+1
		while (x1, y+1) in sand:
			x1 += 1
		if (x1, y+1) not in clay:
			return water, still, False

		x2 = x-1
		while (x2, y+1) in sand:
			x2 -= 1
		if (x2, y+1) not in clay:
			return water, still, False

	flood = True

	while flood == True:
		x1 = x+1
		x2 = x-1

		while (x1, y) not in clay and (x1, y) not in sand:
			sand.add((x1, y))
			if y >= miny:
				water += 1
			if (x1, y+1) not in clay and (x1, y+1) not in sand:
				flood = False
				w, s, flood = water_from_spring(x1, y)
				water += w
				still += s
				break
			x1 += 1

		while (x2, y) not in clay and (x2, y) not in sand:
			sand.add((x2, y))
			if y >= miny:
				water += 1
			if (x2, y+1) not in clay and (x2, y+1) not in sand:
				flood = False
				w, s, flood = water_from_spring(x2, y)
				water += w
				still += s
				break
			x2 -= 1

		y -= 1

		if (x, y) not in sand:
			flood = True
			still += x1-x2-1
			break

		if flood == True:
			still += x1-x2-1

	return water, still, flood

def print_diagram():
	minx = 4000
	maxx = 0

	for c in clay:
		if c[0] < minx:
			minx = c[0]
		if c[0] > maxx:
			maxx = c[0]

	for c in sand:
		if c[0] < minx:
			minx = c[0]
		if c[0] > maxx:
			maxx = c[0]

	for j in range(miny, maxy+1):
		for i in range(minx, maxx+1):
			if (i, j) in clay:
				print('#', end='')
			elif (i, j) in sand:
				print('.', end='')
			else:
				print(' ', end='')
		print()

clay = set()
sand = set()
miny = 4000
maxy = 0

with open('17-in', 'r') as f:
	lines = f.read().strip().split('\n')

	for l in lines:
		parts = l.split(', ')
		c1, val = parts[0].split('=')
		c2, vals = parts[1].split('=')
		n1, n2 = map(int, vals.split('..'))

		for n in range(n1, n2+1):
			if c1 == 'x':
				clay.add((int(val), n))
			elif c1 == 'y':
				clay.add((n, int(val)))

	x = 500
	y = 0

	sand.add((x, y))

	for c in clay:
		if c[1] < miny:
			miny = c[1]
		if c[1] > maxy:
			maxy = c[1]

	print(water_from_spring(x, y))

	print_diagram()
