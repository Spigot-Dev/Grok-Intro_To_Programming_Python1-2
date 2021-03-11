#17/02/21
#What does this code do?
#	The purpose of this code is to add a certain amount of underscores "_" to a japanese happy emoticon. ^_^
#	To do this, we take an input, convert it to a integer (so we can use it in a calculation), and multiply a string (how many times to display the string) by the int. 
#	During this, it is important to keep track of your spaces, as it gets a bit tricky. 

happystr = input("Enter a number: ")

happiness = int(happystr)

print("^" + ("_" * happiness) + "^")


#What is happening here?
#	In the first line of this example, we are taking an input, and assigning it to the "happystr" variable. 
#	We are the using the int() function to convert "happystr" to a string, and assigning it to the "happiness" variable. This is important, because we can't use "happystr" in calculations, as it is a string.
#	We then use the print function to print a carot (^), followed by however many underscores (_) we defined in happystr. It is important we use + here, instead of commas, else we'd get ^ _ _ _ _ ^, instead of ^____^

