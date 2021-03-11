#17/02/2021
#What does this code do?
#	This code is designed to tell you how many days had no rain, based on an input of which days had rain. We can do this using the .split() function.
#	The split() method returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
#	example: str.split(str="", num = string.count(str))
#	parameters: str- this is any delimeter, by default it is space.
#				num- this is the number of lines to be made. 

data = input('Which days had rain? ')
days = data.split()
print('Number of days without rain:', 7 - len(days))

#What is happening here?
#	On line 1, our code takes a day of which days had rain, and assigns the string to the "data" variable. 
#	From there, the code splits the data variable, giving it a list of the days within the "data" string. 
#	Using the len() function, the code decides how many days had rain, and subtracts that number from 7, giving us how many days had no rain. 

