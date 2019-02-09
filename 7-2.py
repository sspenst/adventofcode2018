from collections import defaultdict

with open('7-in', 'r') as f:
	lines = f.read().strip().split('\n')

	post = defaultdict(list)
	req = defaultdict(list)

	for l in lines:
		parts = l.split()
		post[parts[1]].append(parts[7])
		req[parts[7]].append(parts[1])

	avail = {k for k in post.keys() if k not in req}
	order = ''
	workers = 5
	worker = {}
	second = 0

	while len(avail) > 0 or len(worker) > 0:
		# assign available steps to workers
		while len(avail) > 0 and len(worker) < workers:
			nexts = [x for x in avail if len(req[x]) == 0]
			if len(nexts) == 0:
				break
			s = min(nexts)

			worker[s] = 61 + ord(s) - ord('A')

			avail.remove(s)

		# execute second
		for s in list(worker.keys()):
			worker[s] -= 1
			if worker[s] == 0:
				del worker[s]
				order += s
				avail.update(post[s])
				for a in post[s]:
					req[a].remove(s)

		second += 1

	print(second)
