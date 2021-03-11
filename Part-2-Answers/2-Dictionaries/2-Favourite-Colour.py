# 11/03/21
# What does this code do?
#	This code makes a "dictionary" of some different peoples favourite colours. It's designed to take an input, and keep taking inputs, until
#   a blank line is entered. After the while loop is broken, it prints the contents of the dictionary. 

colours = {}

line = input('Name and colour: ')
while line:
  name, number = line.split()
  colours[name] = number
  line = input('Name and colour: ')

for i in colours:
  print(i, colours[i])

# What is happening here?



car[price] = "15000"