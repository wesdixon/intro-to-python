#This program takes a user inputted number and prints whether it is positive, negative or zero

number = int(raw_input("Please enter a number: "))

if number< 0:
	print("This number is negative")
elif number > 0:
	print("This number is positive")
else:
	print("This number is 0")