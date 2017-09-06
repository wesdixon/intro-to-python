def list_product(lst):

    product = 1
    for num in lst:
        product *= int(num)
    return product


user_input = raw_input("Please enter numbers seperated by commas for a list: ")
lst = user_input.split(",")
print list_product(lst)
