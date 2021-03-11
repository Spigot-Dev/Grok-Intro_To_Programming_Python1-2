#17/02/21
#What does this code do?
#	This code is quite simple. It takes an input, and assigns it to the "msg" variable. An If gate then decides whether or not the word Aardvark is contained within "msg" and prints a message based on that. 

msg = input("Enter line: ")
if "aardvark" in msg:
	print("Aardvark!")
else: 
	print("No aardvarks here :( ")
	
#What is happening here?
#	There is no new concepts here. The code takes an input, and assigns it to "msg". 
#	the "If" loop decides if there is the string "aardvark" in the string referenced to by "msg". If there is, the "if" branch runs, printing "Aardvark!"
#	If the conditions are not met, meaning that the string "aardvark" was not in "msg", then the "else" branch would run, printing "No aardvarks here :( "

