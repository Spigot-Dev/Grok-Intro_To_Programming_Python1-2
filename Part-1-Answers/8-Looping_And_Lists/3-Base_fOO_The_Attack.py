#17/02/21
#What does this code do?
#	This code is designed to take an input, and print out the input according to the following conditions:
#	1. Read the words in reverse order
#	2. Only grab the words that start with Capital Letters. 

code = input('code: ')
code = code.split()
code.reverse()
msg = []
for word in code:
  if word[0].isupper():
    msg.append(word.lower())
print('says: ' + ' '.join(msg))

#What is happening here?
#	Our code first takes an input, and assigns it to the "code" variable. 
#	From there, the code splits the string into seperate values, and reassigns the seperated string to "code" 
#	It then puts the variable string in reverse. 
#
#	Our code then creates a new list named [msg]
#	Using a for loop, it decides if the first letter (word[0].isupper()) is uppercase. If it is, it is converted to lowercase, and added to the list [msg]
#	the last line then joins the values within the list together, and prints them. 
