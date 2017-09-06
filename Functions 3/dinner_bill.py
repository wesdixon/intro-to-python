# . Write a function that will calculate the total amount of a dinner bill, given the total before tax,
# the tax rate, and the tip percentage. Your function will accept these three values as arguments. It will then do the following:
#
#  * Apply the tax rate to the bill total.
#  * Apply the tip percentage to the total amount.
#  * Return the total amount of bill before and after tip.
#
#  Here's an example of how we would call the function:
#
#  ```python
#  In [1]: bill_with_tax, bill_with_tax_and_tip = calc_total_bill(100, 0.10, 0.10)
#
#  In [2]: bill_with_tax_and_tip
#  Out[2]: 121.0


def bill_with_tax(before_tax_bill, tax_rate):

    return before_tax_bill * (1.0 + tax_rate)


def calc_total_bill(before_tax_bill, tax_rate, tip_percentage):

    bill_with_taxes = bill_with_tax(before_tax_bill, tax_rate)
    bill_with_taxes_and_tip = bill_with_tax(before_tax_bill, tax_rate) * (1.0 + tip_percentage)

    return bill_with_taxes, bill_with_taxes_and_tip


before_tax_bill = float(raw_input("Please enter the dinner bill, before tax or tip: "))
tax_rate = float(raw_input("Please enter the tax rate (decimal form): "))
tip_percentage = float(raw_input("Please enter the tip percentage (decimal form): "))

bill_with_tax, bill_with_tax_and_tip = calc_total_bill(before_tax_bill, tax_rate, tip_percentage)

print "The bill with tax is {}".format(bill_with_tax)
print "The bill total, with tax and tip included is {}".format(bill_with_tax_and_tip)
