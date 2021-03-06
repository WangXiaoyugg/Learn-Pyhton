#coding:utf-8
# def my_sum(*arg):
# 	if len(args) == 0:
# 		return 0
# 	for val in arg:
# 		if not isinstance(val,int):
# 			return 0
# 	return sum(arg)
# def my_average(*arg):
# 	if len(args) == 0:
# 		return 0
# 	for val in arg:
# 		if not isinstance(val,int):
# 			return 0
# 	return sum(arg)/len(arg)

# print my_sum(1,2,3,4,5)
# print my_sum(1,2,3,4,5,'6')
# print my_average(1,2,3,4,5)
# print my_average()

def my_sum(*arg):
	return sum(arg)
def my_average(*arg):
	return sum(arg)/len(arg)

def dec(func):
	def in_dec(*arg): #my_sum
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val,int):
				return 0
		return func(*arg)
	return in_dec

#dec return in_dec -> my_sum
#my_sum = in_dec(*arg)
my_sum = dec(my_sum)
my_average = dec(my_average) 
print my_sum(1,2,3,4,5)
print my_sum(1,2,3,4,5,'6')
print my_average(1,2,3,4,5)
print my_average()