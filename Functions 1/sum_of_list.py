def sum_of_list(lst):

    sum = 0
    for num in lst:
        sum += int(num)
    return sum

user_input = raw_input("Please enter numbers seperated by commas for a list: ")
lst = user_input.split(",")
print "The sum of these numbers is {}".format(sum_of_list(lst))
