#17/02/21
#What does this code do?
#	This code is designed to make a count down, based off a input value. 

n = int(input('Time to launch: '))
print('Counting down ...')
while n > 0:
  print(n, '...')
  n = n - 1
print('Lift Off!')

#What is happening here?
#	The first line of our code takes an integer input, and assigns it to the "n" variable. 
#	from there, it counts down from "n" to 0, printing line by line, using a while loop. 
#	The while loop states: while n is greater than 0, print n - 1 until, n is equal to 0. 
