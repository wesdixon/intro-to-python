# #This program prompts the user to input numbers separated by commas.
# Your script will then take these inputted numbers and store them as
# a list of tuples, two at a time. Finally, your script will print that list of
# tuples to the user. If the user inputs an odd number of numbers,
# then only make a list of the largest number of pairs of two that are possible.


user_input = raw_input("Enter numbers separated by commas: ")
list_of_tuples = []

inputlist = user_input.split(',')

for index, element in enumerate(inputlist):
    inputlist[index] = element.strip()

index = 0

for element in inputlist:
    if index < (len(inputlist)-1):
        indextuple = (inputlist[index], inputlist[index+1])
        list_of_tuples.append(indextuple)
        index +=2


print list_of_tuples
