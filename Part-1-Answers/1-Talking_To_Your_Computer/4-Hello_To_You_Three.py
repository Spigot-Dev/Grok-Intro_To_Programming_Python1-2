#17/02/21
#What does this code do?
#	The purpose of this code is to take 3 inputs, and assign each to their own variables. 
#	Then, it will take those variables, and print them, in addition to a prefix (young, wise, brave)
#	This is using the "string additon" concept explored in the previous code. 

name1 = input("Friend: ")
name2 = input("Friend: ")
name3 = input("Friend: ")

print("Hello, young " + name1)
print("Hello, wise " + name2)
print("Hello, brave " + name3)

#What is happening here?
#	In this example, same as last time, the output of each iteration of the function "input()" is
#	being assigned to its variable named "name1", "name2" etc.
#
#	We are then using the "print()" function to display each variable, as well as its prefix.
#
#	We join each part of the overall print output eg: Hello, young name1 using the +, so it looks like this:
#	print("String1 " + variable1)
#	It is important that we put the space at the end of string1, before the end quote mark, otherwise, 
#	our output will look like this:
#	code: print("String1" + name1)
#	output: Hello, youngname1
#
#	We want it to look like this:
#	code: print("String1 " + name1)
#	output: Hello, young name1

