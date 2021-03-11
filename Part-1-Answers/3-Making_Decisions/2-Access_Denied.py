#17/02/21
#What does this code do?
#	This code is designed to take a input, and assign it to the variable "password". It then goes into an If/Else statement. If the conditions are met, it will run the "if" branch. If they're not met, the "else" branch will run

attempt = input("Enter Password: ")

if attempt == "chEEzburg3rz":
	print("Access Granted.")
else:
	print("Access Denied.")

#What is happening here?
#	This code, once again introduces a new concept. Else. It works in co-operation with If loops, to make another case, instead of continuing. 
#	In this example, if the "attempt" variable EXACTLY matches the string given (in this case "chEEzburg3rz"), then the If branch will run, meaning the code will print "Access Granted." If the conditions are not met [meaning that 
#	"attempt" didn't match the given string (chEEzburg3rz)] the else branch will run, meaning the code will print "Access Denied."
