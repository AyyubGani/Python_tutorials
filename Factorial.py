print("Hello, this code can easily find the factorial of any whole number.")
print("What is your name?")
#name is asked
name = input()
#name is input
print("Hello", name,"Pick any whole number please.")
#asks for a whole number 
factorial = 1
#variable "factorial" is assigned
number = int(input())
if number < 0:
	#checks if number is negative
	print("Sorry but there are no factorials for negative numbers.")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1,number + 1):
		factorial = factorial*i
	print("The factorial of", number,"is", factorial".")