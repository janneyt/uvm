import numpy as np
import matplotlib.pyplot as plt

'''backLegSensorValues = np.load("data/BackLegTouchSensor.npy")
frontLegSensorValues = np.load("data/FrontLegTouchSensor.npy")
'''
'''plt.plot(frontLegSensorValues, label="Front Leg", linewidth=6)
plt.plot(backLegSensorValues, label="Back Leg")'''
sin_wave = np.load("data/sin_data.npy")
y_arr = [x for x in range(1000)]

plt.plot(y_arr, np.sin(sin_wave))
plt.legend()
plt.show()

