def evens_list(lst):

    return [num for num in lst if int(num) % 2 == 0]

user_input = raw_input("Please enter numbers seperated by commas for a list: ")
lst = user_input.split(",")

print evens_list(lst)
