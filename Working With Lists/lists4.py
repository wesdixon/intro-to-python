#For a user inputted number, write a script that outputs a list of multiples of that
#number from 0 up to another user inputted number.
#For example, given the numbers 4 and 20, your script should print the numbers 4, 8, 12, and 16.

high_number = int(raw_input("Please enter a high end number: "))
multiplier = int(raw_input("Please enter a multiplier: "))

new_list = []

for index in range(1, (high_number+1)):
    if index % multiplier == 0:
        new_list.append(index)

print("The list of multiples from 0 through " + str(high_number) + " by multiplier " + str(multiplier) + " is:")
print new_list
