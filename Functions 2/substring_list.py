 # Write a function that takes in a list of strings, as well as an inputted substring
 # (i.e. another string), and returns a list of the indices of the strings that c
 # ontain that inputted substring. For example, if I input `['This', 'is, 'an' , 'example']`
 # as the list of strings, and `is` as the substring, your function should return `[0, 1]`.

def make_substring_lst(lststr, substr):

    return [index for index, value in enumerate(lststr) if substr in value]

input_words = raw_input("Enter a list of words seperated by commas: ")
lst = input_words.split(",")

input_string = raw_input("Enter a substring: ")

print "The list of indexes in which the substring is present in the matching value is: "
print make_substring_lst(lst, input_string)
