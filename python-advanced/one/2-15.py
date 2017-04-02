# int(12345) => 12345
# int('12345',16) => 74565
# def int(x,base=2):
# 	return int(x,base)
# int2('1000000') => 64

# import functools
# int2 = functools.partial(int,base=2)

# print int2('1000000')
# print int2('1010101')

import functools

sorted_ignore_case = functools.partial(sorted,cmp = lambda s1,s2: cmp(s1.upper(),s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

 