#!/usr/bin/python
import sys
import getopt
import math


def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))

def exact_fibo(n):
	phi = (math.sqrt(5)+1)/2
	phi = phi**n
	phi2 = ((-1)**n)/phi
	return int((phi - phi2) / math.sqrt(5))



def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hn:i:", ["name=", "number="])
	except getopt.GetoptError:
		print('fibonacci.py -n <name> -i <number>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('fibonacci.py -n <name> -i <number>')
			sys.exit()
		elif opt in ("-n", "--name"):
			name = arg
		elif opt in ("-i", "--number"):
			number = int(arg)


	print("Hello {}".format(name))
	if number <= 0:
		print("please enter a positive integer")
	else:
		print(" The fibonacci sequence for the first {} term(s)".format(number))
		for i in range(number):
			print(exact_fibo(i))

if __name__ == "__main__":
	main(sys.argv[1:])