import pyrosim.pyrosim as pyrosim

#where information about my world will be stored
pyrosim.Start_SDF("boxes.sdf")

#identify variables
rows = 5 #number of rows in grid
columns = 5 #number of columns in grid
tower_height = 10 #how tall the tower is gonna be, how many blocks high
start_size = 1.0  # base block size

# Loop to create 10 blocks in the tower
for row in range(rows):
    for column in range (columns):
        #find position for this tower
        x = row
        y = column
        z = start_size / 2

        #generate size at (x,y)
        block_size = start_size
        for level in range (tower_height):
            # Send the cube with the current position and size
            pyrosim.Send_Cube(name = f"Box_{row,column, level}", pos = [x,y,z], size = [block_size, block_size, block_size])

            # Update the size for the next block (reduce by 10% in each dimension)
            z += block_size
            block_size += 0.9 #make each cube 90% of the previous

#close the sdf file
pyrosim.End()

