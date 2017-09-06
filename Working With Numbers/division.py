#This program does division of two numbers without using '/' as would be typical

print ("Please enter positive numbers only: ")

first_int = int(raw_input("Enter a number to be divided:  "))
second_int = int(raw_input("Enter a number of times to divide it:  "))

quotient = 0
remainder = 0

if first_int == second_int:
	quotient = 1

else:
	while first_int >= second_int:
		first_int -= second_int
		quotient += 1
		remainder = first_int
		


print ("This quotient of these two numbers is " + str(quotient) + " with a remainder of " + str(remainder))