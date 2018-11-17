#Input 3 number a<b<c
#print the number starting frin a to c in multiples of B

a=0
b=30
c=300

for x in range (c):
	if (x>=a):
		d=x%b
		if (d==0):
			print x
	
