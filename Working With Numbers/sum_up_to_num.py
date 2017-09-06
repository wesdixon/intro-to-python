#This program computes the sum from 0 to a user inputted number. This time though, start at the user inputted number and work down.

input_number = int(raw_input("Please enter a number: "))

i = input_number
answer = input_number

while i != 0:
	i -= 1
	answer += i
	
print ("The sum from 0 to " + str(input_number) + " is " + str(answer))
