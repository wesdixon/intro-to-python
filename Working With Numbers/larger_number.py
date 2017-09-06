#This program takes two user inputted numbers and prints "The first number is larger" or "The second number is larger" depending on which is larger.

first_number = int(raw_input("Enter the first number: "))
second_number = int(raw_input("Enter the second number: "))

if first_number > second_number:
	print("The first number is larger")
elif first_number < second_number:
	print("The second number is larger")
else:
	print("The two numbers are equal")