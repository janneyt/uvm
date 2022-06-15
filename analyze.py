import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/BackLegTouchSensor.npy")
frontLegSensorValues = np.load("data/FrontLegTouchSensor.npy")

plt.plot(frontLegSensorValues, label="Front Leg", linewidth=6)
plt.plot(backLegSensorValues, label="Back Leg")
plt.legend()
plt.show()
