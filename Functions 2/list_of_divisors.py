# Write a function that takes in a list of numbers, as well as an additional number (i.e. two arguments),
# and returns a list of `yes` or `no` depending on whether each number in the list is divisible by the second number.
# For example, if I input `[10, 25, 36, 12, 20]` as the list of numbers, and `5` as the additional number,
# your function should return `['yes', 'yes', 'no', 'no', 'yes']`.

def divisible_lst(lst,divisor):

    return ["yes" if num % divisor == 0 else "no" for num in lst ]


input_values = raw_input("Please enter a list of numbers seperated by commas, no spaces: ")
input_lst = [int(num) for num in input_values.split(",")]
input_divisor = int(raw_input("Please enter a divisor: "))

print "The altered list with yes if divisor divides evenly or no otherwise is: "
print divisible_lst(input_lst,input_divisor)
