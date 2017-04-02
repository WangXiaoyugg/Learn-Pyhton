# coding:utf-8
# def log(prefix):
# 	def log_decorator(f):
# 		def wrapper(*args,**kw):
# 			print '[%s] %s()...' % (prefix,f.__name__)
# 			return f(*args,**kw)
# 		return wrapper
# 	return log_decorator

# @log('DEBUG')
# def test():
# 	pass
# print test()


# 标准decorator:拆分
# def log_decorator(f):
#     def wrapper(*args, **kw):
#         print '[%s] %s()...' % (prefix, f.__name__)
#         return f(*args, **kw)
#     return wrapper
# return log_decorator

# # 返回decorator:
# def log(prefix):
#     return log_decorator(f)

import time

def performance(unit):
	def performance_decorator(f):
		def wrapper(*args,**kw):
			t1 = time.time()
			r = f(*args,**kw)
			t2 = time.time()
			print 'call %s() in %f%s' % (f.__name__, (t2 - t1),unit)
			return r
		return wrapper
	return performance_decorator


@performance('ms')
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))

print factorial(10 )