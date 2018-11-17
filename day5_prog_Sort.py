#Input 10 integers - Sort them without sort function in list

#integer = ["24", "45", "26", "28", "38", "18", "48", "88", "78", "107"]
#integer = ["9", "6", "5", "7", "8", "4", "2", "3", "0", "1"]
#integer = ["0", "0", "1", "2", "2", "3", "4", "5", "8", "7"]
#integer = ["8", "8", "8", "8", "8", "8", "8", "8", "8", "7"]
#integer = ["8", "8", "8", "8", "8", "8", "8", "8", "8", "8"]
#integer = ["8", "8", "8", "8", "8", "8", "8", "8", "8", "0"]
#integer = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
#integer = ["8", "8", "8", "8", "8", "8", "8", "8", "8", "8"]
#integer = ["800", "8", "8", "8", "8", "8", "8", "8", "8", "7"]
integer = ["8", "8", "8", "8", "-88", "8", "8", "8", "8", "7"]
#integer = ["8", "8", "8", "8", "8", "8", "8", "8", "8", "7.5"]
#integer = ["8"]
#integer = ["8", "7"]
#integer = ["8", "8"]
#integer = ["z", "A", "", "a", "b", "8", "8", "8", "8", "0"]
#integer = ["aaa", "bbb", "xxxx", "8", "8", "8", "8", "8", "8", "0"]

x=len(integer)
a=0
print type(integer[a])
while (a<x):
	integer[a]=int(integer[a])
	a=a+1
print integer
x=0
j=len(integer)
m=0
n=len(integer)
newlist=[]
while m<j-1:
	x=0
	if (integer[x]<integer[x+1]):
		b=integer[x]
	else:
		b=integer[x+1]
	x=x+1
	while x<n:
		if (b<integer[x]):
			x=x+1
		else:
			b=integer[x]
			x=x+1
	if (x>=n-1):
		newlist.append(b)
		if b in integer:
			integer.remove(b)
		n=len(integer)
	m=m+1
newlist.append(integer[0])
print newlist
