#This program computes the least common multiple between two user inputted numbers

lower_num = int(raw_input("Enter the lower number "))
higher_num = int(raw_input("Enter the higher number "))

lcm = higher_num

while lcm % lower_num != 0:
	lcm += higher_num

print ("The least common multiple of these numbers is " + str(lcm))