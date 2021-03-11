#17/02/21
#What does this code do?
#	This code essentially takes 2 inputs, and counts out the difference between the two. 

current = int(input("Current floor: "))
destination = int(input("Destination floor: "))
for i in range(current, destination + 1):
  print("Level", i)
  
#What is happening here?
#	Our first 2 lines take the inputs of the current and destination floor, assigning them as Integers to the variables "current" and "destination" respectively. 
#	From there, the for loop counts out current + 1 until destination is reached. 
