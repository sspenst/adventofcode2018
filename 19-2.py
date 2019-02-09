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
	reg[0] = 1

	while 1:
		if reg[ip] >= len(inst):
			break

		ins = inst[reg[ip]]
		print(reg)
		print(ins)

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

# notes:
# addi 2 16 2
# seti 1 4 1 # reg[1] = 1
# seti 1 2 4 # reg[4] = 1
# mulr 1 4 3 # reg[3] = reg[1] * reg[4]
# eqrr 3 5 3 # if reg[3] == reg[5]: reg[3] = 1
# addr 3 2 2 # go to 1 0 0 if reg[3] == 1
# addi 2 1 2 # reg[2] += 1
# addr 1 0 0 # reg[0] = reg[0] + reg[1]
# addi 4 1 4 # reg[4] += 1
# gtrr 4 5 3 # if reg[4] > reg[5] goto 13
# addr 2 3 2 # reg[2] += reg[3]
# seti 2 7 2 # goto line 4
# addi 1 1 1 # reg[1]++
# gtrr 1 5 3 # if reg[1] > reg[5] goto 17
# addr 3 2 2 # reg[2] += reg[3]
# seti 1 0 2 # reg[2] = 1
# mulr 2 2 2 # reg[2] *= reg[2]
# addi 5 2 5
# mulr 5 5 5
# mulr 2 5 5
# muli 5 11 5
# addi 3 4 3
# mulr 3 2 3
# addi 3 7 3
# addr 5 3 5
# addr 2 0 2
# seti 0 1 2
# setr 2 1 3
# mulr 3 2 3
# addr 2 3 3
# mulr 2 3 3
# muli 3 14 3
# mulr 3 2 3
# addr 5 3 5
# seti 0 9 0
# seti 0 8 2
