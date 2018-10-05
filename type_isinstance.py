class animal(object):
	def run(self):
		print('Animal is running')

class Dog (animal):
	def run(self):
		print('Dog is running')

q=Dog()
q.run()
print(isinstance(q,animal))