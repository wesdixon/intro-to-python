#Alter your script in Part 3, Question 3 to accept arbitrary lists.
#Build it such that the user has to enter 7 numbers (each separated by an enter at the command line) for each list.

list1 = []
list2 = []

print("There will be two constructed lists.  Each list gets 7 numbers.")

for index in range(0,7):
    user_input = int(raw_input("Please enter number {} into List One: ".format(index+1)))
    list1.append(user_input)

for index in range(0,7):
    user_input = int(raw_input("Please enter number {} into List Two: ".format(index+1)))
    list2.append(user_input)

new_list = []

for index in list1:
    if index in list2:
        new_list.append(index)

new_list.sort()

print("The common elements between the two lists: ")
print(list1)
print(list2)
print("Are the elements in the following sorted list: ")
print(new_list)
