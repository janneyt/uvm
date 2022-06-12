
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF ( "boxes.sdf" )

# Cube's physical dimensions
length = 1
width = 2
height = 3

# Position coordinates for cube
x = 0
y = 0
z = height/2

for num in range(0,10):
    pyrosim.Send_Cube ( name="Box"+str(num), pos=[x, y , z+ (height * num)], size=[length-(num/10), width-(num/10), height] )


pyrosim.End ()
