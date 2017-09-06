# This program continually accepts a word from the user. As it does, it should add the word to a set.
# If the user enters the letter `v`, your script should display all the known words, it's vocabulary.
# This will continue until the user enters the letter `q`, which should quit the program.

vocab_set = set()

x = 1

while x == 1:

    user_input = raw_input("Enter a word to add to the vocabulary (Enter v to view words entered or q to quit): ")

    if user_input == "q":
        break

    elif user_input == "v":
        seperator = ", "
        print (seperator.join(vocab_set))

    else:
        vocab_set.update(set([user_input]))
