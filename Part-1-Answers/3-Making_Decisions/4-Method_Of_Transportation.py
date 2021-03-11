#17/02/21
#What does this code do?
#	This code has quite a few steps, so we'll break them down line by line. The overall purpose of this code is to tell you which method of transport to use for your next outing, based on a few different things.
#	It also introduces a new concept, Elif, which is used between an If and an Else, it more or less adds another condition to the If loop, except only if the first condition is met. 
#	The first step is based on the weather. The code takes an input, and tells you whether to take the bus or not, based on whether its raining or not. 
#	From there, your method of transport is based on distance. 
#	The program should only ask for the distance if it's relevant to the case. Meaning, if it's raining, it doesn't need to know how far you're travelling, as you'll be taking the bus. 

weather = input("Is it currently raining? ")
if weather == "Yes" or weather == "yes":
	print("You should take the bus.")

elif weather == "No" or weather == "no":
	distance = int(input("How far in KM do you need to travel? "))
	if distance >10:
		print("You should take the bus.")
	elif distance <2:
		print("You should walk.")
	elif distance >=2 and distance <=10:
		print("You should ride your bike.")

#What is happening here?
#	This code uses multiple loops, and may look confusing, however it's based off a few logic gates.
#	The first line defines our "weather" variable. It takes an input, asking if its raining or not. 
#	After that, the code uses our conditions in the first loop of: If its raining, you should take the bus, If its not raining, it will activate the Elif branch.
#
#	The first part of the Elif branch, asks how far you need to travel, and assigns that integer to the "distance" variable. 
#	Based off that variable, the code will make one of the following decisions:
#	Outcome A: Because your travel distance was less than 2KM, the code will tell you to walk. 
# 	Outcome B: Because your travel distance was Either 2, 8, or between 2 and 8, the code will tell you to ride your bike. 
#	Outcome C: Because your travel distance was greater than 8, the code will tell you to take the bus. 

