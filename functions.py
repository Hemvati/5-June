def ad(p,q):
	x=p+q	
	#print("The sum of",p ," and ",q," is ",x)
	return ('The sum of {} and {} is {}'.format(p,q,x))
def prnt():
	a=int(input("Enter a number:"))
	b=int(input("Enter another number:"))
	print(ad(2,3))
	print(ad(a,b))	
prnt()
