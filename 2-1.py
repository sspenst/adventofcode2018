with open('2-in', 'r') as f:
	lines = f.read().strip().split()

	t2 = 0
	t3 = 0

	for l in lines:
		b2 = False
		b3 = False

		for c in l:
			n = l.count(c)
			if n is 2:
				b2 = True
			elif n is 3:
				b3 = True

		if b2:
			t2 += 1
		if b3:
			t3 += 1

	print(t2)
	print(t3)
	print(t2*t3)
