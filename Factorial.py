#!/usr/bin/python
import sys, getopt

def my_factorial(x):
	"""
	This is my factorial function.
	It is not especially efficient, but, hey, I'm just beginning so bite me.
	"""
	factorial = 1
	for i in range(1, x + 1):
		factorial = factorial*i
	return factorial

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hn:i:",["name=","number="])
	except getopt.GetoptError as e:
		print('Factorial.py -n <name> -i <number>')
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print('Factorial.py -n <name> -i <number>')
			sys.exit()
		elif opt in ("-n", "--name"):
			name = arg
		elif opt in ("-i", "--number"):
			number = int(arg)
	
	print("Hello {}, you want the factorial of the number {}".format(name, number))
	#asks for a whole number 
	factorial = 1
	#variable "factorial" is assigned
	if number < 0:
		#checks if number is negative
		print("Sorry but there are no factorials for negative numbers.")
	elif number == 0:
		print("The factorial of 0 is 1")
	else:
		factorial = my_factorial(number)
		print("The factorial of {} is {}".format(number, factorial))

if __name__ == "__main__":
   main(sys.argv[1:])