d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
n=0
for x in d.itervalues():
    sum = sum+x
    n=n+1
print sum/n

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for v in d.itervalues():
    sum = sum + v
print sum / len(d)