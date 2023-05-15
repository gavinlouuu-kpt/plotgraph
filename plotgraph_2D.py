import datetime
import numpy as np
import matplotlib.pyplot as plt

data_path = 'data/dT.txt'
data = np.loadtxt(data_path, delimiter=',', skiprows = 1)
x_unix_millis = data[:,0]
y1 = data[:,5] #1:temp,2:humidity,3:3V,4:ADC,5:Resistance
y2 = data[:,1] #1:temp,2:humidity,3:3V,4:ADC,5:Resistance


# for txt file with 2D
# Convert Unix time in milliseconds to Unix time in seconds
x_unix_seconds = x_unix_millis / 1000

# Convert Unix time in seconds to datetime objects
x_datetime = []
for unix_time in x_unix_seconds:
    dt_object = datetime.datetime.fromtimestamp(unix_time)
    x_datetime.append(dt_object)

# y_compute_volt = [] #compute y from adc to mV with 0.125mV per bit
# for mv_adc in y:
#     mv_object = mv_adc*0.125
#     y_compute_volt.append(mv_object)


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot the first dataset on ax1 using a blue line
ax1.plot(x_datetime, y1, color='blue', label='y1')

# Plot the second dataset on ax2 using a red line
ax2.plot(x_datetime, y2, color='red', label='y2')

# Set the labels and legend for the chart
ax1.set_xlabel('x')
ax1.set_ylabel('y1', color='blue')
ax2.set_ylabel('y2', color='red')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


# Plot x_datetime against y with 2D
# plt.plot(y)
# plt.plot(x_datetime, y_compute_volt) #Compute volt
plt.plot(x_datetime, y)
# plt.xlabel('Time')
# plt.ylabel('Y values')
# plt.title('My plot')
plt.show()
