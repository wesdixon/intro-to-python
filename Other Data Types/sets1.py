# #This program prompts the user to input numbers separated by commas, and then does so again.
# It should then print those numbers that were common in both entries.

common_set = set()

user_input = raw_input("Please numbers seperated by commas for the first set: ")

inputlist = user_input.split(',')

for index, element in enumerate(inputlist):
    inputlist[index] = element.strip()

set1 = set(inputlist)


user_input = raw_input("Please numbers seperated by commas for the first set: ")

inputlist = user_input.split(',')

for index, element in enumerate(inputlist):
    inputlist[index] = element.strip()

set2 = set(inputlist)

seperator = ", "
print "The numbers that are common in both of these sets are: "
print (seperator.join(set1 & set2))

#could also use:
# print set1.intersection(set2)
