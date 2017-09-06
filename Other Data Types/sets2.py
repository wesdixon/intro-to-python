#This program prompts a user to input a list of words separated by commas, and then prints out the unique words in the list.

user_input = raw_input("Please enter a list of words separated by commas: ")

inputlist = user_input.split(',')

for index, element in enumerate(inputlist):
    inputlist[index] = element.strip()

set1 = set(inputlist)

seperator = ", "

print ("The unique words from this list are: ")
print (seperator.join(set1))
