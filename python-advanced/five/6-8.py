class Person(object):
	def __init__(self,name,gendar):
		self.name = name
		self.gendar = gendar

	def __call__(self,friend):
		print 'My name is %s...' % self.name
		print 'My friend is %s...' % friend

p = Person('Bob', 'male')
p('Tim')