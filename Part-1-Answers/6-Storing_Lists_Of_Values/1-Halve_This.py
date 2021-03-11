#17/02/2021
#What does this code do?
#	This code is designed to take a integer input, assign it to a variable, divide that by two, and assign it to a new variable, which is then converted back to a string, to be printed. 
#Why do we convert the input to an integer, just to change it back to a string?
#	We do this because strings cannot be used in this kind of calculation, and then convert it back because we can't print integers. 

inp = int(input("Number: "))
half = inp/2
halfstr = str(half)
print("Half Number:", halfstr)

#What is happening here?
#	This code gets a bit confusing, due to the numver of variables, so lets break it down. 
#	On line 1, we take the input as an integer, and assign it to the variable "inp"
#	On line 2, we divide "inp" by 2, and assign the result of that equation to "half"
#	On line 3, we convert "half" to a string, and assign it to "halfstr" we do this because we can't print integers.
#	On line 4, we print out "halfstr" as well as some context words, so we're not just blurting out the number. 