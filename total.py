total=0
def sum(a1,a2):
	total=a1+a2
	print("Inside the function local total:",total)
	return total
sum(10,20)
print("Outside the function global total:",total)
