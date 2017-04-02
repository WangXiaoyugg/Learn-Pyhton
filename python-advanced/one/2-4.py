def f(x):
	return x**2

print map(f,[1,2,3,4,5,6,7,8,9])

def format_name(s):
	return s[0].upper() + s[1:].lower()

names = ['adam','LISA','barY']
print map(format_name,names)