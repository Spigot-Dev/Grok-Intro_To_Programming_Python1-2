#17/02/21
#What does this code do?
#	The purpose of this code is to take an input, and until you enter a blank line, append the given input into a list, and ask again. 
#	The program should not count duplicates. 

words = []
word = input('Word: ')
while word != '':
  if word not in words:
    words.append(word)
  word = input('Word: ')
print('You know', len(words), 'unique word(s)!')

#What is happening here?
#	The first line defines a new list, named [words] from there, the next line takes an input, and adds it to a variable named 'word' 
#	A while loop decided if the entry is a blank line or not, and if not, the while loop activates, going straight into a if loop. 
#	If the entered word is not already in the list [words], the word is added, using the .append() function. 
#	The IF loop then ends, going back into the while loop, asking again, for a new word. 
#	Once both loops have ceased, the code prints the length of our list [words] as well as some context words. 
