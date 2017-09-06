#This program obtains the count of a user inputted letter in a user inputted string

input_word = raw_input("Enter a word to be analyzed: ").lower()
input_letter = raw_input("Enter a letter to count in this word: ").lower()

count = 0

for index in list(input_word):
    if index == input_letter:
        count += 1

print ("The letter " + input_letter + " appears " + str(count) + " times in the word " + input_word)
