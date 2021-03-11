#17/02/21
#What does this code do?
#	The purpose of this code is to take an input, by using the "input()" function, assign it to a variable
#	using the "print()" function, we can print the variable, as well as the string "Hello, "
#
#	The "input()" function is designed to be able to take a string input (unless otherwise defined).
#	it is commonly then defined to a variable, which can then be printed, used in calculations, or stored.

name = input("What is your name? ")
print("Hello,", name)

#What is happening here?
#	In this example, the output of the function "input()" is being assigned to the variable named "name"
#	We are then using the "print()" function to display the variable, as well as "Hello,".
#	in the parenthese of "print" we are using a Comma. In this function, the comma dictates a space, 
#	which is far easier than doing:
#	print("string1" + " " + variable1)