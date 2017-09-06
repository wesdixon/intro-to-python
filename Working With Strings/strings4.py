#This program makes every other letter of a user inputted string capitalized.

input_string = (raw_input("Enter a word: "))
new_string = ""

for index, letter in enumerate(list(input_string)):
    if index % 2 == 0:
        new_string += letter.upper()
    else:
        new_string += letter

print ("The word with every other letter capitalized is: " + new_string)
