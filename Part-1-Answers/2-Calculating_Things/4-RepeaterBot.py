#17/02/21
#What does this code do?
#	This code further explores the concept of multiplying strings that we saw in the last one. 
#	Similarly, to do this, we take the 2 inputs, one str and one int, and display the string, however many times specified by the int. 

inp = input("What do you want me to say? ")
num = int(input("How many times do you want me to say it? "))
out = inp*num
print(out)

#What is happening here?
#	We are taking the 2 inputs, "inp" and "num", and multiplying inp by num. 
#	It's important that we define the input of "howmany" as an integer, as we are unable to multiply a string by a string. We can do Str*Int or Int*Int, but not Str*Str. 
#	It's also important to keep track of our parentheses in the howmany line, otherwise we may encounter a syntax error.
#	code: howmany = int(input("BlahBlah? ")
#                   ^F1   ^F2 
#	Because we have 2 functions on this line, we need to make sure we open and close them correctly. The above line needs another closing bracket, because we have only closed the int(), and not the print()
