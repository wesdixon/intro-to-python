#This program computes the factorial of a user inputted number.

input_number = int(raw_input("Enter a number: "))

i = input_number
answer = input_number

while i != 1:
	i -= 1
	answer *= i

print ("The factorial of " + str(input_number) + ", also known as " + str(input_number) + "! is " + str(answer))