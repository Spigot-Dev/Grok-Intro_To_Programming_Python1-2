#17/02/21
#What does this code do?
#	This code is designed to take an input, print each character on a seperate line, and then print the entire string in caps. We can acheive this by using a For loop.
#	For loops are commonly used with counters, which is how we'll be using it in this case. 

cheerin = input('Cheer: ')
for character in cheerin:
  print("Give me a " +character+", " +character+ "!")
print("What does it spell?")
print(cheerin.upper())

#What is happening here?
#	Our code is taking an input, and assigning it to the "cheerin" variable.
#	From there, we go into a For loop. For every character in the variable, print the character twice, as if being cheered by a crowd. 
#	Once there is no more letters left to print, the code prints our given input (cheerin variable) in capitals, as if being yelled by a crowd. 
