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

def cetakHexa(value):
	digit="0123456789ABCDEF"

	remstack = Stack()

	while value > 0:
		rem = value % 16
		remstack.push(rem)
		value = value // 16

	newString=""
	while not remstack.isEmpty():
		newString = newString + digit[remstack.pop()]
	print(newString)

cetakHexa(12)
cetakHexa(31)
cetakHexa(229)
cetakHexa(31519)
