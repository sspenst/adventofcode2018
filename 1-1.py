with open('1-in', 'r') as f:
	print(sum([int(l) for l in f.read().strip().split()]))
