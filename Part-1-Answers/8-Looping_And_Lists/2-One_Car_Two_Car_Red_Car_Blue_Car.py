#17/02/21
#What does this code do?
#	The purpose of this code is to take a string input, assign each value within the string into a list. From there, it should count each occourance of a given term, ie: red & blue.

cars = input('Cars: ')
cars = cars.split()

red = blue = 0
for car in cars:
  if car == 'red':
    red += 1
  elif car == 'blue':
    blue += 1

print('red:', red)
print('blue:', blue)

#What is happening here?
#	In the first line of our code, we are taking a input, and assigning it to the variable "cars"
#	From there, we are splitting the values within the string "cars" is referencing, and reassigning the split string back onto the "cars" variable. 
#	We then enter a for loop, counting how many times the words "red" and "blue" show up in our list, and assign them to the variables "red" and "blue" respectively. 
#	The loop then prints how many occourances of each colour car (red and blue) are within our list. 

