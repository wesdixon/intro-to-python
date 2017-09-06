def are_beers_left(n):

    if n > 0:
        print "Beers left!"
    else:
        print "No beers..."

n = int(raw_input("How many beers are there? "))
are_beers_left(n)
