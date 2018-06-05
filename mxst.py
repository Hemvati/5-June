def mxst():
	s1=str(input("Enter a string:"))
	s2=str(input("Enter another string:"))
	if (len(s1)>len(s2)):
		return s1
	elif (len(s1)==len(s2)):
		print("Both strings are Equal\n",s1,"\n",s2)
	else:
		return s2
print("The largest string is ",mxst())	
