#17/02/21
#What does this code do?
#	This code is designed to identify if a predefined string is within a given input. 

Line = input('Line: ')
words = Line.split()
if 'ROBOT' in words:
  print('There is a big robot in the line.')
elif 'robot' in words:
  print('There is a small robot in the line.')
elif 'robot' in Line.lower().split():
  print('There is a medium sized robot in the line.')
else:
  print('No robots here.')
  
#What is happening here?
#	In this code, we give an input ("line") which is then split, and reassigned into the "words" variable. 
#	From there, the code enters an IF statement, which identifies whether there is a capital case, a lower case, or a mixed case iteration of the word. 
#	Using that information, the code will then print one of the following, depending on the case of the word. 
#	There is a big robot in the line, there is a small robot in the line, there is a medium sized robot in the line. 

