import re
from collections import defaultdict

with open('3-in', 'r') as f:
	lines = f.read().strip().split('\n')

	claims = [map(int, re.findall('-?\d+', l)) for l in lines]

	p = defaultdict(list)
	o = [None]*(len(claims)+1)

	for (n, x, y, w, h) in claims:
		o[n] = False
		for i in range(x, x+w):
			for j in range(y, y+h):
				if len(p[(i, j)]) > 0:
					o[n] = True
					o[p[(i, j)][0]] = True
				p[(i, j)].append(n)

	for i, v in enumerate(o):
		if v == False:
			print(i)
