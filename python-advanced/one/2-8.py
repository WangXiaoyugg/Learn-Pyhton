# def f():
# 	print 'call f()'
# 	def g():
# 		print 'call g()'
# 	return g

# x = f()
# x()

# def myabs():
# 	return abs

# def myabs2(x):
# 	return abs(x)

# def calc_sum(lst):
# 	return sum(lst)

# calc_sum([1,2,3,4])

# def calc_sume(lst):
# 	def lazy_sum():
# 		return sum(lst)
# 	return lazy_sum

# f = calc_sum([1,2,3,4])
# f()


def calc_prod(lst):
	def lazy_prod():
		def f(x,y):
			return x*y
		return reduce(f,lst,1)
	return lazy_prod

f = calc_prod([1,2,3,4])
print f
print f()