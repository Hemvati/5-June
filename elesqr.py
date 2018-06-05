def lst():
	l=list()
	for i in range(1,21):
		e=i**2
		l.append(e)
	print(l)
	print("First 5 values are:",l[0:6])
	print("Last 5 values are:",l[-5:])
lst()
