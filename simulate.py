import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

# Physics setup
physicsClient = p.connect ( p.GUI )
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Load generated robots, world features, etc.
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF ( "world.sdf" )

# Global utility variables
num_iters = 100

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(num_iters)
frontLegSensorValues = np.zeros(num_iters)


for x in range(0,num_iters):

    time.sleep(1/60)
    p.stepSimulation ()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link ( 'BackLeg' )
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link( 'FrontLeg' )

np.save("data/BackLegTouchSensor.npy",backLegSensorValues)
np.save("data/FrontLegTouchSensor.npy",frontLegSensorValues)

p.disconnect ()
