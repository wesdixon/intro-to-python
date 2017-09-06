from random import randint

random = randint(1,100)
guess = 0

while guess != random:

	guess = int(raw_input("Guess a number between 1 and 100:  "))

	if guess == random:
		print("Wow!  You got it right!  The number was " + str(random))
	else:
		if guess > random:
			print("Sorry!  Too high, try again!")
		else:
			print("Dang!  Too low, try again!")