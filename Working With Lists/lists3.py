#Given the list `[0, 3, 6, 9, 10, 2, 5]` and `[2, 6, 4, 7, 8, 1, 15]`, write a script that finds
#the common elements between them.
#Store them in a list, and print that list, sorted, as the final output

list1 = [0, 3, 6, 9, 10, 2, 5]
list2 = [2, 6, 4, 7, 8, 1, 15]

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
