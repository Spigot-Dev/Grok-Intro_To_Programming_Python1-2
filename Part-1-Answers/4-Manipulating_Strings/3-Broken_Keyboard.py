#17/02/21
#What does this code do?
#	The purpose of this code is to take the input, which is your friends weird message, and decipher it. To do this, we use the .replace function. 
#	The .replace function is designed to replace a given string, or a variable with a different string, making it similar to the Find & Replace tool in Microsoft Word. You give it something to replace, and you tell it what to put
#	there instead. 
#	
#	We also use some tricky wizardry with variable redefining. Because python codes run sequentially, if we define a variable at the top of a page, we can redefine it later on, and then all call's of the var AFTER the redefinition
#	will call the new value, as opposed to the original. 

msg = input("What did she say? ")
msg = msg.replace("###", "o")
msg = msg.replace("##", "e")
msg = msg.replace("%%", "a")

print("She meant to say:",msg)
 
#What is happening here?
#	Put simply, the code is going through her message, and whenever it encounters ###, it gets replaced with "o".
#	Whenever it encounters ##, it gets replaced with "e", and whenever it encounters %%, it gets replaced with "a".
#	This works, because according to Grok, we can assume that in any given message there won't be 2 vowels directly next to each other. 
#
#What is the syntax of .replace?
#	Similar to the Find & Replace tool in MS Word, the replace function finds the given string, and replaces it with another. See below for an example.
#	Code:
#
#	msg = "My name is Jeff."
#	newmsg = msg.replace("str to be replaced", "what to replace it with.")
