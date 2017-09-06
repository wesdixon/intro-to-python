def is_a_fan(name):

    fans = set(["Cary", "Josh", "Sean"])
    if name in fans:
        return True
    else:
        return False

user_input = raw_input("Enter name please: ")

if is_a_fan(user_input) is True:
    print "Did you know that {} is a fan of Frozen?!".format(user_input)
else:
    print "Well, {} is not really a fan of Frozen...".format(user_input )
