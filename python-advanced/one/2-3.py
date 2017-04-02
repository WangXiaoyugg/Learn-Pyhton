import math

def add(x,y,f):
	return f(x)+f(y)

def output(x):
	print x

output(add(25,9,math.sqrt))