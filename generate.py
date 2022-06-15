
import pyrosim.pyrosim as pyrosim


legFront = {'name': 'Front Leg',
         'length': 1,
         'width': 1,
         'height': 1,
         'pos': [0.5,0,-0.5]}

legBack = {'name': 'Back Leg',
         'length': 1,
         'width': 1,
         'height': 1,
         'pos':[-0.5,0,-0.5]}


torso = {'name': 'Torso',
         'length': 1,
         'width': 1,
         'height': 1,
         'x': 0,
         'y': 0,
         'z': 2.5}

block = {'name': 'box1',
         'length': 5,
         'width': 2,
         'height': 1,
         'x': 10,
         'y': 10,
         'z': 1.5}
def create_world():

    pyrosim.Start_SDF ( "world.sdf" )
    num = 0
    pyrosim.Send_Cube ( name=block['name'], pos=[block['x'], block['y'], block['z'] + (block['height'] * num)],
                        size=[block['length'] - (num / 10), block['width'] - (num / 10), block['height']] )

    pyrosim.End ()

def create_robot():
    pyrosim.Start_URDF ( "body.urdf" )

    num = 0

    pyrosim.Send_Cube(name='Torso', pos=[0,0,1.5],
                      size=[1,1,1])

    pyrosim.Send_Joint(name='Torso_FrontLeg',parent='Torso',child='FrontLeg', type='revolute', position=[0.5,0,1])
    pyrosim.Send_Cube ( name='FrontLeg', pos=legFront['pos'],
                        size=[1, 1, 1] )

    pyrosim.Send_Joint(name='Torso_BackLeg',parent='Torso',child='BackLeg', type='revolute', position=[-0.5,0,1])
    pyrosim.Send_Cube(name='BackLeg', pos=legBack['pos'],
                      size=[1,1,1])


    pyrosim.End()

# Create robot before world for major performance upgrade
create_robot()

create_world()
