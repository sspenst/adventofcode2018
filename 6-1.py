from collections import defaultdict

def manhattan(x, y, pts):
	dist = []

	mini = -1
	mind = 1000

	for i, pt in enumerate(pts):
		d = abs(pt[0]-x) + abs(pt[1]-y)
		if d == mind:
			return None
		elif d < mind:
			mind = d
			mini = i
		dist.append(d)

	return mini

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

	inf = set()

	for i in range(minx, maxx+1):
		inf.add(manhattan(i, miny, pts))
		inf.add(manhattan(i, maxy, pts))

	for j in range(miny+1, maxy):
		inf.add(manhattan(minx, j, pts))
		inf.add(manhattan(maxx, j, pts))

	inf.discard(None)

	areas = defaultdict(int)

	for i in range(minx+1, maxx):
		for j in range(miny+1, maxy):
			c = manhattan(i, j, pts)
			if c != None:
				areas[c] += 1

	maxa = 0

	for k, v in areas.items():
		if k not in inf:
			if v > maxa:
				maxa = v

	print(maxa)
