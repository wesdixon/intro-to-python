# Write a function that takes in a list of strings, as well as an inputted letter (which looks like a string with a single
# character), and returns a list of only those strings from the input list that end with that letter.
# For example, if I input `['I', 'am', 'in', 'love', 'with', 'Python']` as the list of strings, and `n` as the
# inputted letter, your function should return `['in', 'Python']`.

def ends_with_letter(lst, letter):

    return [word for word in lst if letter == word[-1]]

input_lst = (raw_input("Please enter a list of numbers seperated by commas: ")).replace(" ","").split(",")

input_letter = raw_input("Please enter a letter: ")

print ends_with_letter(input_lst, input_letter)
