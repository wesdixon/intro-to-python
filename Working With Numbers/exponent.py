#This program does exponential computation of two numbers without using '**' as would be typical

print ("Please enter positive numbers only: ")

root = int(raw_input("Enter a root number:  "))
exponent = int(raw_input("Enter a number for the exponent  "))

index = 1
product = root

while index < exponent:
	product *= root
	index += 1


print ("The product of " + str(root) + " raised to a power of " + str(exponent) + " is " + str(product))