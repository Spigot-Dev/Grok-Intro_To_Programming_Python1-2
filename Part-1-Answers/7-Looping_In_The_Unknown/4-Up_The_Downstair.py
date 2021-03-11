#17/02/21
#What does this code do?
#	The purpose of this code, is to take an input, and draw a staircase that corresponds to the input. 

n = int(input("How many steps? "))

print("__")
for i in range(n - 1):
  print('  '*(i + 1) + "|_")
print("__"*n + "|")  

#What is happening here?
#	In the first line, the code takes an input, and converts that to a integer, and assigns it to "n". In this case, "n" is the number of steps in our staircase.
#	After that, the code enters a for loop, that prints another step for every count until 0, from our input number ("n")
#	This continues until we can't go any lower, so the code finishes the staircase. 
