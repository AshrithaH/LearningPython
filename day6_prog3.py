#User Input for date of birth
DoB= raw_input("Enter your Date of birth: ")

#Current_Date=[11, 17, 2018, 16, 48]
Current_Date= raw_input("Enter Current Date: ")
#define days in each month
jan=31
feb=28
march=31
april=30
may=31
june=30
july=31
aug=31
sept=30
october=31
nov=30
dec=31

#conversion of string input to int --> Date of Birth
DoB = DoB.split(":")
print DoB
a=0
for n in DoB:
	DoB[a]=int(DoB[a])
	a+=1

#conversion of string input to int --> Current Date
Current_Date = Current_Date.split(":")
print Current_Date
a=0
for n in Current_Date:
	Current_Date[a]=int(Current_Date[a])
	a+=1

#To find the remaining days in birth year
year1=[12, 31, DoB[2], 23, 59]

if DoB[0]==1:
	#Number of days in month and the number of remaining days in the year, for each year
	RemDays=(jan-DoB[1])+feb+march+april+may+june+july+aug+sept+october+nov+dec
elif DoB[0]==2:
	RemDays=(feb-DoB[1])+march+april+may+june+july+aug+sept+october+nov+dec
elif DoB[0]==3:
	RemDays=(march-DoB[1])+april+may+june+july+aug+sept+october+nov+dec
elif DoB[0]==4:
	RemDays=(april-DoB[1])+may+june+july+aug+sept+october+nov+dec
elif DoB[0]==5:
	RemDays=(may-DoB[1])+june+july+aug+sept+october+nov+dec
elif DoB[0]==6:
	RemDays=(june-DoB[1])+july+aug+sept+october+nov+dec
elif DoB[0]==7:
	RemDays=(july-DoB[1])+aug+sept+october+nov+dec
elif DoB[0]==8:
	RemDays=(aug-DoB[1])+sept+october+nov+dec
elif DoB[0]==9:
	RemDays=(sept-DoB[1])+october+nov+dec
elif DoB[0]==10:
	RemDays=(october-DoB[1])+nov+dec
elif DoB[0]==11:
	RemDays=(nov-DoB[1])+dec
elif DoB[0]==12:
	RemDays=dec-DoB[1]
print ("Remaining days in birth year:" +str(RemDays))
RemHours = Current_Date[3]-DoB[3]
print RemHours
RemMins=Current_Date[4]-DoB[4]
print RemMins

#Calculate years between one year after birth year and one year before current year

NextYears=(Current_Date[2])-(DoB[2]+1)
NextYears=NextYears*365
print ("Remaining Days in the next years: "+str(NextYears))


#Calculate days passed in this year

ThisYear=[01,01,Current_Date[2],23,59]
if Current_Date[0]==1:
	#Number of days passed in current year
	RemDaysThis=Current_Date[1]
elif Current_Date[0]==2:
	RemDaysThis=Current_Date[1]+jan
elif Current_Date[0]==3:
	RemDaysThis=Current_Date[1]+jan+feb
elif Current_Date[0]==4:
	RemDaysThis=Current_Date[1]+jan+feb+march
elif Current_Date[0]==5:
	RemDaysThis=Current_Date[1]+jan+feb+march+april
elif Current_Date[0]==6:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may
elif Current_Date[0]==7:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may+june
elif Current_Date[0]==8:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may+june+july
elif Current_Date[0]==9:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may+june+july+aug
elif Current_Date[0]==10:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may+june+july+aug+sept
elif Current_Date[0]==11:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may+june+july+aug+sept+october
elif Current_Date[0]==12:
	RemDaysThis=Current_Date[1]+jan+feb+march+april+may+june+july+aug+sept+october+nov
print ("Remaining Days in the current year: "+str(RemDaysThis))

#Inc has the number of leap years in between DoB and current date
inc=0
a=DoB[2]
while (a<Current_Date[2]):
#	print ("Iteration")
#	print a
	if ((a%4) ==0):
		pass
		inc=inc+1
		a=a+4
	else:
		a=a+1

Days=RemDays+NextYears+RemDaysThis+inc
print ("Days from birthdate to today: " +str(Days)+ " Hours: " +str(RemHours)+ " Minutes: "+str(RemMins))
