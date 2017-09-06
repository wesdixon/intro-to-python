#This program determines whether or not a user inputted number is a prime number and prints
#`'The number you inputted is (not) a prime number.'` depending on what your script finds.

number = int(raw_input("Enter a number to be tested: "))

is_a_prime = True
divides_by = 0

for index in range(2,number):
    if number % index == 0:
        is_a_prime = False
        divides_by = index
        break

if is_a_prime == True:
	print ("The number you inputted IS INDEED a prime number")
else:
	print ("The number you inputted IS NOT a prime number because it can be evenly divided by " + str(divides_by))
