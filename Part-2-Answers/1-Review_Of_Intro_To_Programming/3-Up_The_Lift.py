#17/02/21
#What does this code do?
#	This is designed to take 2 integer inputs, the Destination Floor (dfloor) and the Current Floor (cfloor)
# and calculate how many levels you need to go up. 

cfloor = int(input('Current floor: '))
dfloor = int(input('Destination floor: '))
for i in range(cfloor, dfloor):
  print('Level', i)
print('Level', dfloor)  

#What is happening here?
#	In this code, There is 2 integers being taken as inputs, then stored as variables "dfloor" and "cfloor" respectively. 
#	The levels between cfloor and dfloor are being counted out line by line using the for loop. 