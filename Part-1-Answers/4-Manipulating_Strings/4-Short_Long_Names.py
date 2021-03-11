#17/02/21
#What does this code do?
#	This code used concepts previously explored, the code takes an input, determines the length of the input using ".len" From there, the code decides what output print, based on the length of the input. 

name = input("Enter your name: ")

length = len(name)

if length <=3:
	print("Hi", name,",you have a short name.")
elif length >=4 and length <=8:
	print("Hi",name,", nice to meet you.")
elif length >8:
	print("Hi",name,", you have a long name.")

#What is happening here?
#	This code is a bit confusing, so lets break it down line by line. 
#	In the first line, we take an input, and assign it to the "name" variable. This means we can call upon it later.
#	Then, we assign the result of len(name) to the variable "length". This just makes it easier to call later, so we're not calling len(name) whenever we need it for a condition in a loop. 
#	We then go into our series of loops. The first statement, IF, runs only if the length is equal to or lesser than 3. 
#	If your input doesn't apply to the first loop, we go into our first ELIF statement. This only runs if your name is between 4 and 8 characters long. 
#	If your name is longer than 8 characters, then you run the final statement, another ELIF. 
