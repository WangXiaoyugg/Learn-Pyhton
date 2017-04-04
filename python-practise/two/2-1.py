# coding:utf-8
# 过滤掉列表中的负数
from random import randint

data = [randint(-10,10) for _ in xrange(10)]

print filter(lambda x: x >= 0, data )

print [for x in data if x >= 0]

res = []
for x in data:
	if x >=0:
		res.append(x)
print res

# timeit filter(lambda x: x >= 0, data )中
# timeit [for x in data if x >= 0] 列表解析快
# 迭代最慢

# 筛选字典
d ={x:randint(60,100),for x in range(1,21)}

{k:v for k,v in d.iteritems() if v > 90}

# 集合解析

s = set(data)

{for x in s if x % 3 == 0}