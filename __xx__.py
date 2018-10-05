class student (object):
	def __init__(self,name):
		self.name=name
		
	def __call__(self):
		print('my name is %s'%self.name)
		
s=student('Tom')
s()