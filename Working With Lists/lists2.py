#This program creates a list of only numbers divisible by a user inputted number that are
#between 0 and a user inputted number

new_list = []

high_number = int(raw_input("Please enter a top end number: "))
divisor = int(raw_input("Please enter a divsor to check the numbers between 0 and your entered number: "))

for index in range(0,(high_number+1)):
    if index % divisor == 0:
        new_list.append(index)

print ("The list of numbers between 0 and " + str(high_number) + " that are evenly divide by " + str(divisor) + " is:")
print (new_list)
