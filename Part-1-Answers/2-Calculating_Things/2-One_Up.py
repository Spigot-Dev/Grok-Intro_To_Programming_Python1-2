#17/02/21
#What does this code do?
#	This code takes an input AS AN INTEGER, adds 1 to it, and then prints it out.
#	It's essential that we define the input as an integer (by using "int()") otherwise it'll be treated
#	as a string, and therefore will throw an error when we try to put it in a calculation.

str = input("Please enter a number: ")

num = int(str)
new_num = num + 1

print(new_num)

#What is happening here?
#	In the first line of this example, we are taking an input ("input()") & assigning it to the variable "str"
#	After that, we are using the "int()" function to convert our input (which is by default classed as string)
#	Converting it to an integer (number) means we can use it in calculations. We assign our new integer to the
#	variable "num". 
#
#	We then add 1 to num, and assign it to the variable "new_num", and then print it using "print()"
#
#	To do this differently, and in a more compact way, we could do the following:
#	code: str = input("Please enter a number: ")
#		  
#	      num = int(str)
#		  print(num + 1)
#
#	All this does is remove the need for the "new_num" variable, as we are doing the calculations inside of
#	the print function. 
