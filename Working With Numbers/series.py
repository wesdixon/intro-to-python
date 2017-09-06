#This program outputs the value for "nth" element in the series defined in the picture in this folder

user_input = int(raw_input("Enter an nth element in this series: "))

index = 0
element = 1

while index < user_input:
	element = (2*element) + 1
	index += 1

print ("The value for the element number " + str(user_input) + " in the series is " + str(element))