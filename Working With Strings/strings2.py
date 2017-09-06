#This program checks if a user inputted string ends in an exclamation point.
#**If it does**, then print the string in all capital letters.
#**If it doesn't**, print the string in all lowercase letters.

print ("The word you enter will be capitalized if it ends in an '!' or made into lowercase if it doesn't")
input_word = raw_input("Please enter a word: ")

if input_word[-1] == "!":
    print input_word.upper()
else:
    print input_word.lower()
