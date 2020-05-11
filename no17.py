class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

def revString(words):
	s = Stack()
	for index in range (0, len(words)):
		s.push(words[index])

	for word in words.split(" "):
		s.push(word)

	result = ""
	while not s.isEmpty():
		result += s.pop()

	return result

print(revString("apple "))
print(revString("x "))
print(revString("1234567890 "))