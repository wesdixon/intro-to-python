#This program computes the factorial of a user inputted number using for loops.
#using a call to a function

def compute_factorial(n):

    answer = 1

    if n == 0:
        return 0

    for index in range(1,(n+1)):
        answer *= index

    return answer



input_num = raw_input("Please enter a number: ")

print ("The factorial of " + input_num + ", also known as " + input_num + "! is " + str(compute_factorial(int(input_num))))
