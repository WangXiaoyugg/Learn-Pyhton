passline = 60

def func(val):
	passline = 90
	if val >= passline:
		print 'pass'
	else:
		print 'failed'
	def in_func():
		print val
	in_func()

def Max(val1, val2):
	return max(val1, val2)

# func(80)
print Max(80,90)
# passline = 60

# def func(val):
# 	if val >= passline:
# 		print('pass')
# 	else:
# 		print('failed')

# def Max(val1,val2):
# 	return max(val1,val2)

# print max(90,100)
# # func(89)