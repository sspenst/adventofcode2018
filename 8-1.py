def metadata(data, start):
	child = data[start]
	entries = data[start+1]
	sum = 0

	start += 2

	for i in range(child):
		temp, start = metadata(data, start)
		sum += temp

	for i in range(entries):
		sum += data[start+i]

	return sum, start + entries

with open('8-in', 'r') as f:
	data = list(map(int, f.read().strip().split()))

	print(metadata(data, 0)[0])
