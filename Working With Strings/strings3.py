#This program removes all of the vowels in a user inputted string.

input_word = raw_input("Please enter a word: ")
new_string = ""

vowels = ["a", "e", "i", "o", "u"]

for index in list(input_word):
    if index.lower() not in vowels:
        new_string += index

print ("The new word without vowels (a, e, i, o, u) is: " + new_string)
