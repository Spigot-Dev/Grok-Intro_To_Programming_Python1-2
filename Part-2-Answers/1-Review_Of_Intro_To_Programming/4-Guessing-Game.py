#11/03/21
#What does this code do?
#	This code is designed to act like a robot guessing game. It works via a simple while loop. The only new thing introduced here is the "!="
#   The "!=" or Not Equal To symbol, is part a commonly used family of symbols used in programming. These are: >, <, <=, >=, == and !=. 
#   It more or less states that: while <case> is not equal to (!=) <condition>, run this loop. 

print("What is my favourite food?")
guess = input("Guess? ")
while guess != "electricity" or guess != "Electricity":
  print("Not even close.")
  guess = input('Guess? ')
print("You guessed it! Buzzzz") 

#What is happening here?
#	In this code, a string input is being taken via an input, and assigned to <guess>. The next line (line #9) is the beginning of the While loop. 
#   This loop states, that while <guess> is NOT equal to "electricity" or "Electricity", state that you aren't close
#   and prompt you for another guess. 
#
#   An important part of this code is on line #9, when the loop is initialised. In particular, the addition of "or guess != 'Electricity'"
#   This is important, because without this, if the user entered "Electricity", which is techincally a correct answer, the code wouldn't count it,
#   because it's not the exact string "electricity."
#   
# 
# This loop breaks when <guess> is equal to "electricity" or "Electricity."
#