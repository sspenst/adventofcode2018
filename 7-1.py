from collections import defaultdict

with open('7-in', 'r') as f:
	lines = f.read().strip().split('\n')

	post = defaultdict(list)
	req = defaultdict(list)

	for l in lines:
		parts = l.split()
		post[parts[1]].append(parts[7])
		req[parts[7]].append(parts[1])

	steps = {k for k in post.keys() if k not in req}

	order = ''

	while len(steps) > 0:
		s = min([x for x in steps if len(req[x]) == 0])

		order += s
		steps.remove(s)
		steps.update(post[s])

		for a in post[s]:
			req[a].remove(s)

	print(order)
