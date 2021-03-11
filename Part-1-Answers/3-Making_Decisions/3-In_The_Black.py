#17/02/21
#What does this code do?
#	This code is designed to take a integer input, assign it to a variable (number) decide if its below 0, and print a string based on that output. 
#	We also introduce a new loop operator here, which is >=. That mean Greater than or Equal to. 

number = int(input("Number: "))
if number >= 0:
	print("In the black :) ")
else: 
	print("In the red :( ")
	
	
#What is happening here?
#	The first line in this example is taking in integer input, and assigning it to the variable "number".
#	With this variable, it is using an If/Else statement with the >= operator, to decide if the value of "number" if less than 0. 
#	If number is greater or equal to 0, then it will run the "if" branch of the code, because the conditions are met, meaning it will print "In the black :)"
#	However, if its conditions are not met, meaning that number was less than 0, it will run the else branch of the code, therefor printing "In the red :("
