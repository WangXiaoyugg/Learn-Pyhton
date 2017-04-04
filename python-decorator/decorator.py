

def dec(func):
	print 'call dec'
	def in_dec(*arg): #my_sum
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val,int):
				return 0
		return func(*arg)
	return in_dec

@dec #my_sum = dec(my_sum)
def my_sum(*arg): #my_sum = in_dec
	return sum(arg)
my_sum(1,2,3,4,5)

def my_average(*arg):
	return sum(arg)/len(arg)