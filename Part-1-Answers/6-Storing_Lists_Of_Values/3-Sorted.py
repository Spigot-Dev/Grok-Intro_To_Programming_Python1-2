#17/02/21
#What does this code do?
#	This code is designed to take a single line input of the class, which according to Grok will be given in Title case (Only first letter capitalised.) with a single space between each name.
#	We use the .sort() function in this code, as well as the .split() function. Put basically, the sort() function puts things in order. Ie: letters in alphabetical order, and numbers in ascending order. 

data = input("Students: ")
students = data.split()
students.sort()
print("Class Roll")
for student in students:
  print(student)
  
#What is happening here?
#	Our code is taking an input, of all the students names, on a single line, and assigning that string to the "data" variable. 
#	From there, it splits "data" into seperate words (the students names) and assigns them to a list ("students")
#	It then sorts the list alphabetically, and then prints it line by line using a for loop.
