#To check if the input is pallindrome

UserInput=raw_input("Enter a value: ")
UserInput=UserInput.strip() #strip space in input

x=0
y=len(UserInput)
while y/2>0:
	if UserInput[x]==UserInput[y-1]:
		x+=1
		y=y-1
	else:
		print ("Your input is not a pallindrome")
		exit()
print ("Your input is a pallindrome")


	



