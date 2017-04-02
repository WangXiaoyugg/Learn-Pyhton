import math

def is_odd(x):
	return x % 2 == 1

print filter(is_odd,[1,4,6,7,9,12,17])

def is_empty(str):
	return str and len(str.strip()) > 0

print filter(is_empty,['test',None,'','str',' ','END'])

def is_sqrt(x):
	r = int(math.sqrt(x))
	return r**2 == x

print filter(is_sqrt,range(1,101))