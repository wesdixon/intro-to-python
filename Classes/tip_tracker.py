# This class instantiates an object that represents a waiter, and it passes in a parameter of the
# default tip amount.  Then you can call a method to add a bill (with or without actual tip amount)
# and also call another method to return the total amount earned in tips.  Lastly, if you invoke the
# len() function on the object, the total amount of tips is returned.

class TipOutTracker():

    def __init__(self, default_tip_amount):

        self.default_tip_amount = default_tip_amount
        self.waiter_bills_tips = []


    def __len__(self):

        return len(self.waiter_bills_tips)


    def add_bill(self, bill_amount, tip_amount = None):

        if tip_amount == None:
            tip_amount = self.default_tip_amount
        self.waiter_bills_tips.append((bill_amount, tip_amount))


    def total_tip_out(self):

        return sum([bill * tip_rate for bill, tip_rate in self.waiter_bills_tips])


#Main test block.  Instantiating a waiter, with standard tip rate of 18%

tot = TipOutTracker(0.18)
tot.add_bill(58.90, 0.15)
tot.add_bill(58.90, 0.15)
tot.add_bill(58.90, 0.15)
tot.add_bill(58.90, 0.15)
tot.add_bill(31.58)
tot.add_bill(81.44, 0.20)
tot.add_bill(58.90, 0.15)
tot.add_bill(58.90, 0.15)
tot.add_bill(58.90, 0.15)
tot.add_bill(58.90, 0.15)
tot.add_bill(31.58)
tot.add_bill(81.44, 0.20)

print "The total amount of tips for this waiter is {}".format(len(tot))
print "The total amount earned in tips is ${}".format(tot.total_tip_out())
