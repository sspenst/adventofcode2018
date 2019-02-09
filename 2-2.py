with open('2-in', 'r') as f:
	lines = f.read().strip().split()

	for i in range(len(lines[0])):
		a = []

		for l in lines:
			s = l[:i] + l[i+1:]
			if s not in a:
				a.append(s)
			else:
				print(s)
				exit()
