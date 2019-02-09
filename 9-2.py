class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

with open('9-in', 'r') as f:
	words = f.read().strip().split()
	players = int(words[0])
	marbles = int(words[6]) * 100

	circle = Node(0)
	circle.prev = circle
	circle.next = circle
	score = [0]*players

	for i in range(1, marbles+1):
		if i % 23 == 0:
			circle = circle.prev.prev.prev.prev.prev.prev.prev
			score[(i - 1) % players] += i + circle.data

			circle.prev.next = circle.next
			circle.next.prev = circle.prev
			circle = circle.next
		else:
			circle = circle.next

			newCircle = Node(i, circle, circle.next)
			circle.next = newCircle
			newCircle.next.prev = newCircle
			circle = newCircle

	print(max(score))
