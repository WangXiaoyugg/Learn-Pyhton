sum=0
x=1
while True:
	x=x+1
	if x>100:
		break
	if x%2==1:
		continue
	sum = sum+x
print sum