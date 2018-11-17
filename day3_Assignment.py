#Input an integer - max 256
#1. Find the number of ones in binary
#2. Print the same in binary
#3. Repeat the same for a negative number


x= input("The base 10 value is")
y=1
if (x>255):
	print ("Choose a number smaller than 255")
	exit()
z=x&y #and with 1
if(z==1): #the result is 1 only if the lsb is 1
	Binary="1"
	inc=1 #to get the number of 1s
else:
		Binary="0"
		inc=0
x=x>>1 #to drop the lsb
z=x&y #Repeat...
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary
x=x>>1
z=x&y
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary
x=x>>1
z=x&y
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary
x=x>>1
z=x&y
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary
x=x>>1
z=x&y
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary
x=x>>1
z=x&y
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary
x=x>>1
z=x&y
if(z==1):
	Binary="1"+Binary
	inc+=1
else:
		Binary="0"+Binary	
print Binary
print inc
