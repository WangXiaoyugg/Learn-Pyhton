1.LEGB : L > E > G >B
2.闭包
3. 装饰器

- LEGB
L : locol函数内部作用域
E : enclosing函数内部与内嵌函数之间
G : global全局作用域
B : build-in 内置作用域


- 函数是一个对象
- 函数执行完成后内部变量回收
- 函数属性
- 函数的返回值
- 闭包把内部函数的返回值变成外部函数的属性f.__closure__

1.封装
2.代码复用

- 装饰器
1. 装饰器用来装饰函数
2. 返回一个函数对象
3. 被装饰函数的标识符指向返回的函数对象
4.语法糖 @deco