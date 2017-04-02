def f(x,y):
	return x +y

print reduce(f,[1,2,4,5,6])

print reduce(f,[1,2,3],100)

def prod(x,y):
	return x*y

print reduce(prod,[2,4,5,7,12])

print 2*4*5*7*12