# 11/03/21
# What does this code do?
#	This code introduces a new idea, Dictionaries. The codes purpose is to take an input, and convert it into the numbers you'd need to press
#   on an alphanumeric keypad, as shown in the picture. 

# How do Dictionaries work?
#   To use our dictionary, we first need to initialise it. We can do this as follows:
#   Syntax: <DICTNAME> = {'Key1':'Value1'}
#   Example: MyPetSounds = {"Cat":"Meow", "Dog":"Woof"}
#   To explain further, dictionaries work in a Key and Value paired system. To create an entry, you need to define 2 things,
#   The key (or how the entry will be called), and then the value (What will be referenced when the key is called.) They are seperated by a colon. 


# A dictionary containing the letter to digit phone keypad mappings.
KEYPAD = {
    'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
    'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
    'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
    'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
    'Z': '9',
}
word = input("Enter word: ")
for key in word:
    print(KEYPAD[key], end='')
print() 

print("This code was created by $pigot.")


# What is happening here?
#	In the first 6 lines of this code, we are simply initialising our dictionary. We are associating the numbers on the keypad, to the 3 or 4
#   letters that they can enter. 