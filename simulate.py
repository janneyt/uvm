import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from math import pi
import random

# Physics setup
physicsClient = p.connect ( p.GUI )
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Load generated robots, world features, etc.
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF ( "world.sdf" )

# Global utility variables
num_iters = 1000

# Setup sensors for simulation
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(num_iters)
frontLegSensorValues = np.zeros(num_iters)

# Variables for motor commands
amplitude = pi/4
frequency = 32
phaseOffset = 0

backAmp = pi/4
backFreq = 32
phaseOffsetBack = 0


targetAngles = [amplitude * np.sin(frequency * x + phaseOffset) for x in np.linspace(0,2*pi,num_iters)]
targetAnglesBack = [backAmp * np.sin(backFreq * x + phaseOffsetBack) for x in np.linspace(0,2*pi,num_iters)]
np.save("data/sin_data.npy", targetAngles)
#exit()

for x in range(0,num_iters):

    time.sleep(1/600)
    p.stepSimulation ()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link ( 'BackLeg' )
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link( 'FrontLeg' )


    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = "Torso_FrontLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition =  targetAngles[x],

        maxForce = 10 )

    pyrosim.Set_Motor_For_Joint (

        bodyIndex=robotId,

        jointName="Torso_BackLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition= targetAnglesBack[x],

        maxForce= 10 )


np.save("data/BackLegTouchSensor.npy",backLegSensorValues)
np.save("data/FrontLegTouchSensor.npy",frontLegSensorValues)

p.disconnect ()
