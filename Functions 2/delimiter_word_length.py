#Write a function that counts the number of words in an inputted string,
#where we consider words to be separated by a delimiter.
#Function will return a list of individual word length

def count_words(string, delimiter=" "):

    return [len(word) for word in string.split(delimiter)]

input_string = raw_input("Please enter a string of words seperatred by a chosen delimiter (space is default): ")
input_delimiter = raw_input("Please enter a delimiter that separates the words ")

print "The list of individual word lengths from the string is: "
print count_words(input_string,input_delimiter)
