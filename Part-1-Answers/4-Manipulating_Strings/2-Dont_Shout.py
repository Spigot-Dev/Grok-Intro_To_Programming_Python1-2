#17/02/21
#What does this code do?
#	This code introduces the ".lower()" concept. It is designed to take an input, which'll be in UPPERCASE, and convert it to lowercase, and then print the converted input. 
#	The .lower() function is designed to convert a string, or a variable to lowercase, meaning that all the letter within will be in LC. 

upperc = input("Loud: ")
lowerc = upperc.lower()

print("Quiet:",lowerc)
#What is happening here?
#	This code is super simple. All it does is take an input, and assigns it to the "upperc" variable. (According to Grok, this input will be in uppercase.) It then converts this uppercase variable, to lowercase using the .lower
#	function. The syntax of this is as follows: var.lower()  var being the variable to be converted, and .lower being the function. 
#	The code then prints our converted variable, as well as stating that it is "quiet".
#       AN IMPORTANT NOTE ABOUT ".lower()" You must put in the parenthese' at the end of the .lower, otherwise it won't work!

