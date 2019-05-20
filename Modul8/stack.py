class Stacks(object):
	"""This Class is for Make A Stack"""
	def __init__(self):
		# Function for make a stacks
		self.item=[]

	def pop(self):
		a=self.item.pop()
		print(a)

	def add(self, newData):
		self.item.append(newData)

myStacks=Stacks()
myStacks.add(1)
myStacks.add(2)
myStacks.add(3)
myStacks.pop()
