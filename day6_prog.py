#To check if the input is pallindrome

UserInput=raw_input("Enter a value: ")
UserInput=UserInput.strip()
n=len(UserInput)
x=0
newlist=[]
nextlist=[]

for n in UserInput:
	newlist.append(n)
	x+=1
print newlist

x=len(newlist)
for n in newlist:
	nextlist.append(newlist[x-1])
	x-=1
print nextlist

y=len(nextlist)
a=0
while y>0:
	if newlist[a]==nextlist[a]:
		a+=1
		y=y-1
	else:
		print ("Your input is not a pallindrome")
		exit()
print ("Your input is a pallindrome")


	



