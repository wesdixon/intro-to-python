def print_all_divisors(input_number):

    i = input_number

    while i != 0:
    	if input_number % i == 0:
    		print (str(i) + " is a divsor of " + str(input_number))
    	i -= 1


input_number = int(raw_input("Please enter a number: "))

print_all_divisors(input_number)
