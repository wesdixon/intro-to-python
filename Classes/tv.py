# Let's build a `TV` class, used to represent a television.
#
# 1. In this class, we'll have the following attributes:
#
# * `brand` - `str` holding the brand of the television ('Sony', 'LG', etc.)
# * `on_status` - `bool` holding whether or not the television is on. This should default to False (e.g. off).
# * `current_channel` - `int` holding the current channel number. If the television is off, then the `current_channel`
# should be 0. Given that `on_status` defaults to off, what does that mean the `current_channel` should default to?
# * `life_perc` - `float` holding the percentage of life left in the TV. This should start out at 100% (i.e. default to 100).
#
# 2. Instances of the `TV` class will have the following methods:
#
# * `hit_power` - this will turn the television on/off, depending on whether it's already on/off (if its on it'll switch it off,
# and vice versa). We'll add a couple of stipulations with this one:
# * Each time the television is turned off, it loses a little bit of life - decrease the `life_perc` by 0.01 each time the
# television is turned off.
# * Each time the television is turned off the channel should be set to 0.
# * `change_channel` - this will take in an `int` to change the channel to a new one. We'll add a stipulation to this as well:
# * If the television is not on, but the `change_channel` method is called, print 'Television is not on!'. Otherwise,
# change the channel to the inputted channel.


class TV():

    def __init__(self, brand, on_status=False, current_channel=0, life_perc=100.0):

        self.brand = brand
        self.on_status = on_status
        self.current_channel = current_channel
        self.life_perc = life_perc


    def hit_power(self):

        if self.on_status is False:
            self.on_status = True

        else:
            self.on_status = False
            self.life_perc -= 0.01
            self.current_channel = 0

    def change_channel(self, change_channel_to):

        if self.on_status is False:
            print "Television is not on!"

        else:
            self.current_channel = change_channel_to


#Main test Block

my_tv = TV("Samsung")

my_tv.hit_power()
my_tv.hit_power()
my_tv.hit_power()
my_tv.hit_power()
my_tv.hit_power()
my_tv.hit_power()
my_tv.hit_power() 


my_tv.change_channel(99)

print my_tv.current_channel
print my_tv.life_perc
