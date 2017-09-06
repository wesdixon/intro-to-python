#This program determines whether or not a user inputted number is a prime number and prints
#`'The number you inputted is (not) a prime number.'` depending on what your script finds.
#Refactoring to include a function call

def check_if_prime(n):

    is_a_prime = True
    divides_by = 0

    for index in range(2,n):
        if n % index == 0:
            return False

    return True

number = int(raw_input("Enter a number to be tested: "))

if check_if_prime(number) is True:
	print ("The number you inputted IS INDEED a prime number")
else:
	print ("The number you inputted IS NOT a prime number")
