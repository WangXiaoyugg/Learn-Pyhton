def add(x,y,f):
	return f(x) + f(y)

def output(x):
	print x

output(add(-10,10,abs))