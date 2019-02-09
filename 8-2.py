def metadata(data, start):
	child = data[start]
	entries = data[start+1]
	sum = 0

	start += 2

	if child == 0:
		for i in range(entries):
			sum += data[start+i]
	else:
		nodes = []

		for i in range(child):
			value, start = metadata(data, start)
			nodes.append(value)

		for i in range(entries):
			j = data[start+i] - 1
			if j < len(nodes):
				sum += nodes[j]

	return sum, start + entries

with open('8-in', 'r') as f:
	data = list(map(int, f.read().strip().split()))

	print(metadata(data, 0)[0])
