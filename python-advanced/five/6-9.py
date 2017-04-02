class Fib(object):
    def __call__(self,num):
        a,b,L = 0 ,1,[]
        for n in range(num):
            L.append(a)
            a,b = b,b+a
        return L
f = Fib()
print f(10)