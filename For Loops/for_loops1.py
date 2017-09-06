#This program computes the factorial of a user inputted number using for loops.

input_number = int(raw_input("Enter a number: "))

i = input_number
answer = 1

for index in range(1,(input_number+1)):
    answer *= index

print ("The factorial of " + str(input_number) + ", also known as " + str(input_number) + "! is " + str(answer))
