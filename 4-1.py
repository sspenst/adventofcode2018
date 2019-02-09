import datetime
import re
from collections import defaultdict

def sleep_seconds(sleep):
	seconds = 0
	for i in range(0, len(sleep), 2):
		seconds += (sleep[i+1] - sleep[i]).seconds
	return seconds

with open('4-in', 'r') as f:
	lines = f.read().strip().split('\n')

	times = {}

	for l in lines:
		t, s = l.split('] ')

		y, m, d, h, i = map(int, re.findall('\d+', t))

		times[datetime.datetime(y, m, d, h, i)] = s

	sleep = defaultdict(list)
	guard = None

	for time in sorted(times.keys()):
		if times[time] == 'wakes up':
			sleep[guard].append(time)
		elif times[time] == 'falls asleep':
			sleep[guard].append(time)
		else:
			guard = re.search('\d+', times[time]).group(0)

	g = max(sleep.keys(), key = (lambda k: sleep_seconds(sleep[k])))

	mins = defaultdict(int)

	for i in range(0, len(sleep[g]), 2):
		for j in range(sleep[g][i].minute, sleep[g][i+1].minute):
			mins[j] += 1

	m = max(mins.keys(), key = (lambda k: mins[k]))

	print(int(g)*m)
