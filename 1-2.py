with open('1-in', 'r') as f:
	nums = [int(l) for l in f.read().strip().split()]

	f = 0
	a = [0]

	for n in nums:
		f += n
		if f not in a:
			a.append(f)
		else:
			print(f)
			exit()

	while 1:
		for n in nums:
			f += n
			if f in a:
				print(f)
				exit()
