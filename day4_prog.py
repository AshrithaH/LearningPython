#Define list of 20 elements
#have duplicates
#remove all duplicates
#Error handling

newlist = ["abc", "def", "efg", "hij", "klm", "abc", "def", "efg", "hij", "klm", "abc", "def", "efg", "hij", "klm", "abc", "def", "efg", "hij", "klm", "abc", "def", "efg", "hij", "klm"]
#newlist =["1","2","1","2","1"]
i=0
print newlist
nextlist=[]
for x in newlist:
	a=newlist[i]
	if a not in nextlist:
		nextlist.append(a)
	i=i+1
print nextlist	