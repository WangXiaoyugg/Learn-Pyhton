#coding:utf-8
# passline = 60
# def func(val):
# 	if val >= passline:
# 		print ('pass')
# 	else:
# 		print ('failed')
# 	def in_func():
# 		print val
# 	in_func()
# 	return in_func

# f = func(89)
# f()
# print f.__closure__

# def func_150(val):
# 	passline = 90
# 	if val >= passline:
# 		print '%d pass' %val
# 	else:
# 		print 'failed'
# def func_100(val):
# 	passline = 60
# 	if val >= passline:
# 		print '%d pass' %val
# 	else:
# 		print 'fail'

# func_150(89)
# func_100(89)

def set_passline(passline):
	def cmp(val):
		if val >= passline:
			print '%d pass' %val
		else:
			print '%d failed' %val
	return cmp

f_100 = set_passline(60)
f_150 = set_passline(90)
print type(f_100)
print f_100.__closure__
f_100(89)
f_100(59)
f_150(90)