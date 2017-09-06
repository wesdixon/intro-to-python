#This program computes and prints all of the divisors of a user inputted number.

input_number = int(raw_input("Please enter a number: "))

i = input_number

while i != 0:
	if input_number % i == 0:
		print (str(i) + " is a divsor of " + str(input_number))
	i -= 1