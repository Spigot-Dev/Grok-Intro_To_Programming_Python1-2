#17/02/21
#What does this code do?
#	This code uses the "len()" function to calculate the length of a given variable, or string,
#	The length of our string or variable, is how many characters long it is.	

a = input("Enter text: ")
print(len(a))

#What is happening here?
#	In this example, the first  line is taking an input, and assigning it to the variable "a".
#	Then, the code is printing (displaying) the length of our variable. 
#	
#	It's important to remember the following:
#	1: We use double parenthese'. This is because we are putting another function within the print:
#	print(len(a))
#	^F1    ^F2   
#
#	2: Because we are referencing a variable within Len, it will tell us the length of the string that 
#	the variable is defined as. 
#	Example:
#	code: a = "ABC123"
#		  print(len(a))
#	output: 6
#
#	This happens because the variable, "a" is defined to the string "ABC123", which is 6 characters long.
# 
#	If we were to do this instead:
#	code: print(len("a"))
#	output: 1
#
#	This happens, because the len function (within print) isn't referencing a variable, but referencing a 
#	string insteadm that's why the quotation marks are so important.
#	If we didn't put the quotation marks, we would get the following:
#	code: print(len(a))
#	output:  Traceback (mose recent call last):
#				File "<stdin>", line 1, in <module>
#			 NameError: name 'a' is not defined.
#
#	We get this error, because without the quotation marks, the code thinks we are referencing variable a,
#	Which in this case, isn't defined, because we didn't define it by doing:
#	a = "whatever you want the value of a to be"