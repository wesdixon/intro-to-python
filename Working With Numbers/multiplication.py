#This program does multiplication of two numbers without using '*' as would be typical

first_int = int(raw_input("Please enter first number "))
second_int = int(raw_input("Please enter second number "))

i = 0
product = 0

while i < second_int:
	product += first_int
	i += 1


print ("This prodcut of these two numbers is " + str(product))