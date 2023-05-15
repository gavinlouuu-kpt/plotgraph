import matplotlib.pyplot as plt
import numpy as np

filename = 'data/Parsed/103_12_PID_ratio.txt'  # Replace with the name of your txt file

# Read the data from the file
with open(filename, 'r') as file:
    lines = file.readlines()

# Extract the values into two separate lists
x_values = []
y_values = []

for line in lines:
    x, y = line.strip().split(',')
    x = float(x.strip('[]'))
    y = float(y.strip('[]'))
    x_values.append(x)
    y_values.append(y)

y_compute_volt = [] #compute y from adc to mV with 0.125mV per bit
for mv_adc in y_values:
    mv_object = mv_adc*0.0078125
    y_compute_volt.append(mv_object)

# Plot the graph
plt.plot(y_compute_volt)
plt.xlabel('X Values')
plt.ylabel('mV')
plt.title('Voltage difference of PID sensor')

plt.show()

save_file = filename + "_ratio"
np.savetxt(save_file+".txt", y_values, delimiter=",")
