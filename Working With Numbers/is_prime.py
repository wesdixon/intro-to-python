#This program determines whether or not a user inputted number is a prime number and prints 
#`'The number you inputted is (not) a prime number.'` depending on what your script finds.

number = int(raw_input("Enter a number to be tested: "))

index = 2

is_a_prime = True


while index < number:
	if number % index == 0:
		is_a_prime = False
		break
	index += 1

if is_a_prime == True:
	print ("The number you inputted IS INDEED a prime number")
else:
	print ("The number you inputted IS NOT a prime number")
