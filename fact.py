def fact():
	n=int(input("Enter a number:"))
	if(n%3==0):
		print("Fizz")
	if(n%5==0):
		print("Buzz")
	if((n%3==0) and (n%5==0)):
		print("FizzBuzz")
fact()
