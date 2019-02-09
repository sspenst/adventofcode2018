from collections import defaultdict

with open('6-in', 'r') as f:
	lines = f.read().strip().split('\n')

	pts = []
	minx = 1000
	maxx = 0
	miny = 1000
	maxy = 0

	for l in lines:
		x, y = map(int, l.split(', '))
		pts.append((x, y))

		if x > maxx:
			maxx = x
		if x < minx:
			minx = x
		if y > maxy:
			maxy = y
		if y < miny:
			miny = y

	total = 0

	for i in range(minx+1, maxx):
		for j in range(miny+1, maxy):
			size = 0
			for pt in pts:
				size += abs(pt[0]-i) + abs(pt[1]-j)
			if size < 10000:
				total += 1

	print(total)
