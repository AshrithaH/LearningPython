#Basics
##Print Statements
'''print ("Hello Ash")'''

##If condition
if 1<2 :
 print ("Correct")

##Input - int
test=input("Enter a number:")

##Input - String
test=raw_input("Enter a string:")

##Multiline Comment
'''this 
is 
a 
comment'''

##Single Line Comment

'#This is also a comment'

##Assignment Character '=' 
a=1
print a
a='b'
print a

##Printing With Variable string
Age= 'awesome'
print("My Age is " + Age)

##Escape Character '\' to use "
print "\""

#Numbers
##Arithmetic Calculations
a=1
b=2
c=a+b
print a+b

##Complex Number, j
a=1
b=1.3
c=20j
print a,b,c

##Exponentional Number - To the power of, e
a=-1
print 4-a
a=10e4
print a

##type() Function
print type(a)
print type(b)
print type(c)
print type(Age)

##Type casting
x=int(6.1)
x=float(2.987656)
x=str("acx")
print type(x)

#Strings

##Calling by position 
str="Ashritha"
print str[0]

##From Position 0 to 3
print str[0:3]

##len() function to find teh length of string
print len(str)

##strip() function to strip spaces before or after string
strip1="  my name is ashritha"
print strip1.strip()

##upper() function to convert string to upper
upper1="Varun"
print upper1.upper()
print upper1

##lower() function to convert string to lower
lowe1="Ashritha"
print lowe1.lower()
print lowe1

##replace() function to replace character
replace1="Ashritha"
replace2="Noone"
print replace1.replace ("A",replace2)
print replace1

##split() function to split the string when teh split element is present
split1="WhySplitkjhkjp,mjbj"
print split1.split("p")


