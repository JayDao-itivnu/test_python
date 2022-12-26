from readFromtxt import readFromtxt
import numpy as np
import matplotlib.pyplot as plt
import os
data_dir = "/data"
dir = os.path.join(os.getcwd(), "data")
file = readFromtxt(dir,'x1_1_711.txt')

data_origin = file.readtxt(24)
x_origin = data_origin[0]
y_origin = data_origin[1]

plt.plot(x_origin[1:10],y_origin[1:10])
plt.title('Original plot with noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mA)')
plt.show()