# # Write a script that will continually prompt the user for a set of three things to be separated by commas.
# The first two things will be (x, y) coordinates of the word that follows (the word will be the third thing).
# So the user will input a string that is formatted like `x, y, word`.
# Your script will use the string to build a dictionary with the first two inputs (i.e. the (x, y)) from each string as keys to a dictionary,
# and the third input (the word) as the value for that key. The script will continually prompt the user to input strings in this format until
# the user inputs nothing (i.e. hits enter with no input).
# #
# #  After building the dictionary, your script should allow the user to query the dictionary it built by accepting strings of the format `x, y`.
# It should check if the coordinate is in the dictionary, and if it is return the corresponding word. If it isn't, it should print `Coordinate not found`.
# This should continue until the user inputs the letter `q`, at which point the script should exit.
# #
# #  Example usage:
# #  ```
# #  Please enter a coordinate-word pair in the format (x, y, word): 1, 2, hello
# #  Please enter a coordinate-word pair in the format (x, y, word): 2, 3, world
# #  Please enter a coordinate-word pair in the format (x, y, word):
# #  Please enter a coordinate to look up: 2, 3
# #  world
# #  Please enter a coordinate to look up: 3, 4
# #  Coordinate not found
# #  Please enter a coordinate to look up: q
# #  ```

main_dict = {}

#The section is where the user is prompted to enter coordinate-word pairs

x = 1

while x == 1:

    user_input = raw_input("Please enter a coordinate-word pair in the format (x, y, word)(Press enter to move on): ")

    if user_input == "":
        break

    inputlist = user_input.split(',')

    for index, element in enumerate(inputlist):
        inputlist[index] = element.strip()

    x_coor = inputlist[0]
    y_coor = inputlist[1]
    word_value = inputlist[2]

    to_add_dict = {(x_coor, y_coor) : word_value}

    main_dict.update(to_add_dict)

#This section is where the user is prompted for a coordinate to look up

x = 1

while x == 1:

    user_input = raw_input("Please enter a coordinate to look up (or q to quit): ")

    if user_input.strip() == "q":
        break

    inputlist = user_input.split(',')

    for index, element in enumerate(inputlist):
        inputlist[index] = element.strip()

    coordinates = (inputlist[0],inputlist[1])

    if coordinates in main_dict.keys():
        print main_dict[coordinates]
