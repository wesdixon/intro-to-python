#This program computes the greatest common divisor between two user inputted numbers.

first_num = int(raw_input("Enter the first number: "))
second_num = int(raw_input("Enter the second number: "))

if first_num == second_num:
	greatest_divsor = first_num

else:
	i = 1
	while i < first_num:
		if (first_num%i) == 0 and (second_num%i) == 0:
				greatest_divsor = i
		i += 1

		

print ("The greatest common divisor between these two numbers is " + str(greatest_divsor))


For one of the assignments, I was writing an if statement combining two conditions with "and".  I got different results between (equation and equation == number) compared with (equation == number and equation == number) with the first way performing unexpected.  Do you have to use the