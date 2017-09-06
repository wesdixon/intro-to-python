#This program prints the sum of the whole numbers between 1 and the user inputted number

number = int(raw_input("Please enter a number: "))

answer = 1
i = 1

while i < number:
	i += 1
	answer += i
	

print ("The sum of the whole numbers between 1 and " + str(number) + " is " + str(answer))