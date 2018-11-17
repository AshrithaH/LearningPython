#Interpreted Language
#bytecode
# Memory - Register, Cache, Rom, Ram, Harddisk, nrteork storage (db, raid, nas, san, cloud db)
# Define an integer age and display as my age is "age"
age=29
print("My age is: " +str(age))

Text=raw_input("Enter text\n")
#Text="qwertyuiopasdfghjklbguhyvhgyhvgyvvgyvhgybgybybghyhgffh"



print Text
n=len(Text)
print n
if (n<50):
	exit()
if (n>150):
	exit()

#Question 3

a=n/5 
z=n-(a*5)
print a
print z

if (z>0):
	string="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
	string=string[0:z+1]
		
Text=Text+string
n=len(Text)
a=n/5
print Text
strip1=Text[0:a] 
print strip1
b=a
c=a+a
strip2=Text[b:c]
print strip2
b=c
d=a+a+a
strip3=Text[b:d]
print strip3
b=d
e=a+a+a+a
strip4=Text[b:e]
print strip4
b=e
f=a+a+a+a+a
strip5=Text[b:f]
print strip5
#Question 2
print ("UPPER: "+strip1.upper()+" lower: "+strip1.upper())
print ("UPPER: "+strip2.upper()+" lower: "+strip2.upper())
print ("UPPER: "+strip3.upper()+" lower: "+strip3.upper())
print ("UPPER: "+strip4.upper()+" lower: "+strip4.upper())
print ("UPPER: "+strip5.upper()+" lower: "+strip5.upper())

#Question 4
integer= input("Enter an integer\n")
integer=str(integer)
replace1=strip1.replace("h",integer)
print replace1
replace2=strip2.replace("h",integer)
print replace2
replace3=strip3.replace("h",integer)
print replace3
replace4=strip4.replace("h",integer)
print replace4
replace5=strip5.replace("h",integer)
print replace5
