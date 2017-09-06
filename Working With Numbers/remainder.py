#This program divides one number by another only if it divides evenly with no remainder

first_num = int(raw_input("Enter a number to be divided: "))
second_num = int(raw_input("Enter a number that will do the dividing: "))

remainder = first_num % second_num

if remainder == 0:
	print("Great!  The number " + str(first_num) + " can be evenly divided by " + str(second_num) + " and the result is " + str(first_num/second_num))
else:
	print("Sorry, this number has a remainder of " + str(remainder))