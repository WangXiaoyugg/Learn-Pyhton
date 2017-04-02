# 笔记

- map
map()是 Python 内置的高阶函数，
它接收一个函数 f 和一个 list，
并通过把函数 f 依次作用在 list 的每个元素上，
得到一个新的 list 并返回。

- reduce
reduce()函数也是Python内置的一个高阶函数。
reduce()函数接收的参数和 map()类似，
一个函数 f，一个list，
但行为和 map()不同，
reduce()传入的函数 f 必须接收两个参数，
reduce()对list的每个元素反复调用函数f，
并返回最终结果值

- filter
filter()函数是 Python 内置的另一个有用的高阶函数，
filter()函数接收一个函数 f 和一个list，
这个函数 f 的作用是对每个元素进行判断，
返回 True或 False，
filter()根据判断结果自动过滤掉不符合条件的元素，
返回由符合条件元素组成的新list

注意: s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，

- sorted
Python内置的 sorted()函数可对list进行排序
但 sorted()也是一个高阶函数，
它可以接收一个比较函数来实现自定义排序，
比较函数的定义是，传入两个待比较的元素 x, y，
如果 x 应该排在 y 的前面，返回 -1，
如果 x 应该排在 y 的后面，返回 1。
如果 x 和 y 相等，返回 0。

对于比较函数cmp_ignore_case(s1, s2)，
要忽略大小写比较，
就是先把两个字符串都变成大写（或者都变成小写），
再比较。

Python的函数不但可以返回int、str、list、dict等数据类型，
还可以返回函数！

因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量。

高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，
计算 f(x)=x2 时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
map(lambda x: x*x, [1,2,3,4,5,6])
def f(x):
	return x*x

关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数
匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。

sorted([1,2,3,4],lambda: x,y: -cmp(x,y)) => [4,3,2,1]
 myabs = lambda x: -x if x < 0 else x 

- 装饰器
1. 定义函数
2. 动态添加功能
3. 不想修改函数代码

def f1(x):
  return x*2
def f2():
   return x*x
def f3():
	return x*x*x

1.直接修改函数定义

def f1(x):
  print 'call f1()'
  return x*2
def f2():
  print 'call f2()'
  return x*x
def f3():
  print 'call f3()'
  return x*x*x

2. 高阶函数
1. 接受函数作为参数
2. 可以返回函数
3. 是否可以接受一个函数，对其包装返回一个新函数

def f1(x):
	return x*2
def new_fn(f): => 装饰器
	def fn(x):
	   print 'CALL'+ f.__name__+'()'
	   return f(x)
	return fn

f1 = new_fn(f1)
print f1(5)

@new_fn
def f1(x):
	return x*2

def f1(x):
	return x*2
f1 = new_fn(f1)

- 装饰器的作用

1. 简化代码
打印日志：@log
检测新能：@performance
数据库事务：@transaction
URL路由：@post('./register')

- 包=>模块=>变量
```# test.py => 自身模块名
import p1.util => 引用p1.util模块
print p1.util.f(2,10) => 调用p1.util模块的函数
```
- 包下必须有个__init___.py文件

- 安装第三方模块
1. easy_install
2. pip
- 查找模块 https://pypi.python.org/

- 面向对象 数据封装,继承、多态

- 高阶函数
- 闭包
- 匿名函数
- 装饰器

- 模块的名字避免冲突
- 引用模块
- __future

- 类和实例
- 继承、多态,多重继承

- 定制类
- 特殊目的
- 类型转换
- __call__