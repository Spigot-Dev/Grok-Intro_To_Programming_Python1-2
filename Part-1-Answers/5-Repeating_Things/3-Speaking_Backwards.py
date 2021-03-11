#17/02/21
#What does this code do?
#	This code is designed to take an input, and assign it to a variable, then print that variable backwards. 
#	This can be achieved using indexes.

text_in = input("Line: ")
backwards_text = text_in [::-1]
print(backwards_text)

#What is happening here?
#	Our code is taking a string input, and assigning it to the "text_in" variable. 
#	Using indexes, ([::-1]), we can send all the characters in the string to the opposite end. The code does that to "text_in", and then assigns the result to "backwards_text"
#	It then prints the "backwards_text" variable. 

