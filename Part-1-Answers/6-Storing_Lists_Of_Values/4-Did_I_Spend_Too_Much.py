#17/02/21
#What does this code do?
#	This code is designed to take an input, split the string into different values, and add them to a list. From there, it's meant to add up the sum of the list, to help you work out if you stayed to budget this winter. 

data = input("Enter the expenses: ")
expenses = data.split()
expenses = [int(i) for i in expenses]
a = sum(expenses)
t = str(a)
print("Total: $" + t)

#What is happening here?
#	In the first line, the code is taking an input, and assigning the string to "data"
#	From there, it splits the string into seperate words, and assigns them to a list ("expenses")
#	Using a for loop, it converts each value within the list to an integer, so it can use them in calculations. 
#	We then add up all the values within the list, and assign it to "a"
#	We convert "a" to a string, so it can be printed, and assign it to "t"
#	Print t, as well as some context words. 
