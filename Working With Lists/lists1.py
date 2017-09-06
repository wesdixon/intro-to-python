#This program creates a list of only the even numbers between 0 and a user inputted number.

created_list = []

user_input = int(raw_input("Enter a number to use: "))

for index in range(0,user_input):
    if index % 2 == 0:
        created_list.append(index)

print ("The list of even numbers from 0 through " + str(user_input) + " is: ")
print created_list
