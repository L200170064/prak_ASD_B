class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.item = []

	def isEmpty(self):
		return len(self) == 0

	def __len__(self):
		return len(self.item)

	def peek(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.items[-1]

	def pop(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.item.pop()

	def push(self, data):
		self.item.append(data)

nilai=Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
    	nilai.pop()

print(nilai.item)
