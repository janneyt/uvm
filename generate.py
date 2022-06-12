
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

pyrosim.Send_Cube ( name="Box", pos=[x, y, z], size=[length, width, height] )
pyrosim.Send_Cube ( name="Box", pos=[x, y, z], size=[length, width, height] )
pyrosim.End ()
