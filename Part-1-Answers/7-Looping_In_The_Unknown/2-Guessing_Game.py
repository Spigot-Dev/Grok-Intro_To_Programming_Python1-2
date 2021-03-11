#17/02/21
#What does this code do?
#	This code is designed to ask you to guess a string. It will keep asking you to guess until you are correct. 

print("What is my favourite food? ")
guess = input("Guess? ")
while guess != "electricity":
	print("Not even close.")
	guess = input("Guess? ")
print("You guessed it! Buzzzz")

#What is happening here?
#	The first line is simply printing the question. The 2nd line, takes an input (your 'guess') and assigns it to the "guess" variable. 
#	The while loop states, while your guess isn't electricity, print "not even close."
#	This loop will keep repeating until you guess electricity. 
#	When you finally guess electricity, the loop will break, and the code will print "You guessed it! Buzzzz"