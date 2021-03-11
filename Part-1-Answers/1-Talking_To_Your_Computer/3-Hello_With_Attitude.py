#17/02/21
#What does this code do?
#	The purpose of this code is quite similar to the last one, except we are introducing something called
#	"string concatenation" or put simply, "string addition", because all it is doing is 
#	adding 2 strings together. 

name = input("What is your name? ")
print("So you call yourself" + " " + name + " " + "huh?")

#What is happening here?
#	In this example, same as last time, the output of the function "input()" is being assigned
#	to the variable named "name"
#
#	We are then using the "print()" function to display the variable, as well as a few other things.
#	in the parenthese of "print" we are using (" "). In this function, that just indicates a space.
#	which is more effort than doing the following, however can be used for different things. 
#	print("string1", variable1)
#	
#	For example, the plus is useful for when you need to use integers, or numbers instead of strings. 
#	If you tried doing 1+1 in a print function, using the comma instead of the +, it would do this:
#	code: print(1,1)
#	output: 1 1
#
#	Instead, we want to do:
#	code: print(1+1)
#	output: 2
