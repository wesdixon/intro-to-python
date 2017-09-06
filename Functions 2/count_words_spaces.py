#Write a function that counts the number of words in an inputted string,
#where we consider words to be separated by spaces.

def count_words(s):

    return len(s.split(" "))

input_string = raw_input("Please enter a string of words seperatred by spaces: ")

print "The number of words in the string is {}".format(str(count_words(input_string)))
