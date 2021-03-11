#17/02/21
#What does this code do?
#	This code is designed to take every 3rd letter out of a given input, and disregard the rest, assigning every 3rd letter of the string to 1 variable, "code".
#	We then use a for loop, to repeat that process until there is no more letters left in the string.

code = input("Message? ") [0::3]
msg = ""
for i in code: msg += " " + i
print(msg [1:])

#What is happening here?
#	In this code, we are taking every 3rd letter from an input, and assigning it to the "code" variable.
#	From there, we enter our for loop, which repeats the (msg += " " + i) process until there is no more letters left in "code"
#	Finally, the code prints out the new message. 