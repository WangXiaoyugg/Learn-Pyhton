import math

def quadratic_equation(a, b, c):
    delta = b*b -4*a*c
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    return x1,x2
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)