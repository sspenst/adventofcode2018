with open('9-in', 'r') as f:
	words = f.read().strip().split()
	players = int(words[0])
	marbles = int(words[6])

	circle = [0]
	cur = 0
	score = [0]*players

	for i in range(1, marbles+1):
		if i % 23 == 0:
			cur = (cur - 7) % len(circle)
			score[(i - 1) % players] += i + circle.pop(cur)
		else:
			cur = (cur + 1) % len(circle) + 1
			circle.insert(cur, i)

	print(max(score))
