with open('19-in', 'r') as f:
	lines = f.read().strip().split('\n')

	ip = int(lines[0].split()[1])
	del lines[0]

	inst = [l.split() for l in lines]

	for i in inst:
		for j in range(1, 4):
			i[j] = int(i[j])

		cmd = i[0]

		i[0] = cmd[:3]
		i.insert(1, cmd[3])

	reg = [0]*6

	while 1:
		if reg[ip] >= len(inst):
			break

		ins = inst[reg[ip]]

		#print(ins)

		if ins[0] == 'add':
			if ins[1] == 'r':
				reg[ins[4]] = reg[ins[2]] + reg[ins[3]]
			else:
				reg[ins[4]] = reg[ins[2]] + ins[3]
		elif ins[0] == 'set':
			if ins[1] == 'r':
				reg[ins[4]] = reg[ins[2]]
			else:
				reg[ins[4]] = ins[2]
		elif ins[0] == 'mul':
			if ins[1] == 'r':
				reg[ins[4]] = reg[ins[2]] * reg[ins[3]]
			else:
				reg[ins[4]] = reg[ins[2]] * ins[3]
		elif ins[0] == 'eqr':
			if ins[1] == 'r':
				if reg[ins[2]] == reg[ins[3]]:
					reg[ins[4]] = 1
				else:
					reg[ins[4]] = 0
			else:
				print('OOPS')
		elif ins[0] == 'gtr':
			if ins[1] == 'r':
				if reg[ins[2]] > reg[ins[3]]:
					reg[ins[4]] = 1
				else:
					reg[ins[4]] = 0
			else:
				print('OOPS')

		reg[ip] += 1
	print(reg)	

