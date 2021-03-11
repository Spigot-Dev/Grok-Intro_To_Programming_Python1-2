#17/02/21
#What does this code do?
#	This code is designed to take a string input, and identify if the string contains Anagrams. 

words = input("Enter words: ")
words = words.split()
word1 = words[0]
letters1 = list(word1)
letters1.sort()
word2 = words[1]
letters2 = list(word2)
letters2.sort()

if letters1 == letters2:
  if word1[0] == word2[0] and word1[-1] == word2[-1]:
    print('Super Anagram!')
  else:
    print('Huh?')
else:
  print('Huh?')
  
#What is happening here?
#	This code is a bit tricky, so lets break it down line by line.
#	Line 1 is taking an input, and assigning it to the variable "words"
#	Line 2 breaks the string up, and reassigns it to the "words" variable.
#	Line 3 assigns the first word within the "words" var to the variable "word1"
#	Line 4 breaks up the variable "word1" into letters, and appends them into a list named [letters1], and then line 5 sorts them alphabetically. 
#	Line 6 Repeats the same process of breaking it up, except with the 2nd word. 
#	From there, we enter a IF loop, which decides if the lists are exactly the same, which if they are Anagrams, they should be. 