#17/02/21
#What does this code do?
#	The purpose of this code is to ask Ali, what the password is. If he guesses correctly, the program prints "The cave door opens!", if he doesn't ,the code does nothing. 

attempt = input("What is the password Ali? ")
if attempt == "Open Sesame!":
	print("The cave door opens!")

#What is happening here?
#	This code introduces a new concept. Loops. In this, we use the "if:" function, which more or less decides if A, you go into the loop, or B, you continue through the code, effectively "skipping" the loop. 
#	If loops have a few different parts, there is the definition (If, Else, Elif, For), the condition (a == b, a != b, a => b, etc) and then if you have multiple conditions, you could also use AND, OR, or both of them.
#	
#	The important part to know here, is that loops can be very particular. If you specify ==, then the condition has to be exact. 
#	Loops are also quite particular about their syntax. Below is the proper structure of an If loop:
#
#	Code: 
#	if varA == "Open Sesame":
#		function()
#
#Now lets break it down line by line:
#	Line 1: if varA == "Open Sesame":
#			^Def.   ^Condition      ^ VERY IMPORTANT!!! This colon indicates the end of the loop's definition line. Everything that is indented once underneath this line, will be a part of this loop, until you remove the indent. 
#	Line 2: 	function()
#			^Indented ^Function
#			The indentation here is very important. This means that the function is a part of this loop, and will only run if the loops conditions are met. 

