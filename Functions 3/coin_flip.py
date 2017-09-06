# import random
#
#  def flip_coin():
#      '''
#      Input:  None
#      Output: Str - 'H' for head or 'T' for tail
#
#      Perform an "experiment" using random.random(), return 'H' if result is above .5, 'T' otherwise.
#      '''
#      pass
#
#  def roll_die():
#      '''
#      Input:  None
#      Output: Int - Between 1 and 6
#
#      Using random.randint(), perform a die roll and return the number that "comes up".
#      '''
#      pass
#
#  def flip_coin_roll_die(n_times):
#      '''
#      Input:  Int - number of times to flip a coin and roll a die
#      Output: List - of tuples with the outcomes
#         of the flips and rolls from each time
#      '''
#      pass
#  ```

import random

def flip_coin():

    random_num = random.random()
    if random_num > 0.5:
        return "H"

    return "T"

def roll_die():
    '''
    Input:  None
    Output: Int - Between 1 and 6

    Using random.randint(), perform a die roll and return the number that "comes up".
    '''
    return random.randint(1,6)

def flip_coin_roll_die(n_times):
    '''
    Input:  Int - number of times to flip a coin and roll a die
    Output: List - of tuples with the outcomes
    of the flips and rolls from each time
    '''
    return [tuple([flip_coin(), roll_die()]) for num in range(1,n_times)]


times_to_play = int(raw_input("Enter number of times to flip coin and roll dice: "))
print flip_coin_roll_die(times_to_play)
