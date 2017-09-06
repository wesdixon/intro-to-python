#Write a function that counts the number of words in an inputted string,
#where we consider words to be separated by a delimiter.

def count_words(string, delimiter=" "):

    return len(string.split(delimiter))

input_string = raw_input("Please enter a string of words seperatred by a chosen delimiter (space is default): ")
input_delimiter = raw_input("Please enter a delimiter that separates the words ")

print "The number of words in the string is {}".format(str(count_words(input_string, input_delimiter)))
