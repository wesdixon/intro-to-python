#This program prompts the user for a state name.
#It will then check that state name against the dictionary below to give back
#the capital of that state.
# If the user inputs the name of a state that isn't in the dictionary,
# your script should print that the capital is unknown.

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                        'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                        'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

input_state = raw_input("Please enter a state name: ")
input_state = input_state.lower()

print ("The capital of {} is {}".format(input_state.capitalize(), state_dictionary.get(input_state.capitalize(), "unknown based on this dictionary...")))
