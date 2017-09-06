#This program prompts the user to input numbers separated by dashes ( - ).
#Your script will take those numbers, and print a dictionary where the keys are
#the inputted numbers, and the values are the squares of those numbers.

user_input = raw_input("Enter numbers separated by dashes (-): ")
squares_dict = {}

inputlist = user_input.split('-')

for index, element in enumerate(inputlist):
    inputlist[index] = int(element.strip())

for key in inputlist:
    index = {key : (key*key)}
    squares_dict.update(index)

print("The constructed dictionary of these entries as the keys and their values as their squares is:")
print squares_dict
