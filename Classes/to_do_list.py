# This time you are going to create a class that allows you to keep track of a to-do list.
# The kinds of things that we'd want to be able to do with a to-do list (no pun intended) are:
#
# * Add a to-do item.
# * Mark a to-do item as completed and remove it.
# * Have the length of the to-do list return the number of items you have to do.

class ToDoList():

    def __init__(self):

        self.to_do_lst = []


    def __len__(self):
        #Return number of items on list
        return len(self.to_do_lst)


    def add_to_do(self, to_do_str):

        self.to_do_lst.append(to_do_str)


    def print_all_to_dos(self):

        for item_num, to_do in enumerate(self.to_do_lst):
            print "Item number {} on your to do list is:  {}".format((item_num+1), to_do)


    def completed_to_do(self, num_to_remove):

        del(self.to_do_lst[num_to_remove-1])
        print "Great.  Item number {} on your to do list was removed.  Now your list looks like:".format(num_to_remove)
        self.print_all_to_dos()


# Main test Block

me = ToDoList()
me.add_to_do("Walk the cat")
me.add_to_do("Iron my shirt")
me.add_to_do("Clean the toilet")
me.add_to_do("Think about stuff")

x = 1

while x == 1:

    choice = raw_input('What do you want to do?  Enter "add" to add to the list, or "complete" to check it off: ')
    print ""

    if choice == "add":
        new_to_do = raw_input("\nEnter the new thing to add to the list:  ")
        me.add_to_do(new_to_do)
        print "Great, that was added.  Your list now looks like:\n"
        me.print_all_to_dos()


    elif choice == "complete":
        print "\nOkay, remove an item.  Here's the list, enter the number of the item to remove:"
        me.print_all_to_dos()
        item_to_remove = int(raw_input("Enter item:"))
        print ""
        me.completed_to_do(item_to_remove)
        print ""
