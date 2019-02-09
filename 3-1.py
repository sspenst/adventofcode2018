import re
from collections import defaultdict

with open('3-in', 'r') as f:
	lines = f.read().strip().split('\n')

	claims = [map(int, re.findall('-?\d+', l)) for l in lines]

	p = defaultdict(int)

	for (n, x, y, w, h) in claims:
		for i in range(x, x+w):
			for j in range(y, y+h):
				p[(i, j)] += 1

	print(sum(v > 1 for v in p.values()))
