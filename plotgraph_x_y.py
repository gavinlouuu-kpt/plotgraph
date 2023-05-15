import datetime
import numpy as np
import matplotlib.pyplot as plt

data_path = 'data/Heater_repsonse_01.txt'
# data = np.loadtxt(data_path, delimiter=',', skiprows = 1)
data = np.loadtxt(data_path, delimiter='\t', skiprows = 1)
x_unix_millis = data[:,0]
y = data[:,2] 

# x_unix_seconds = x_unix_millis / 1000 # Convert Unix time in milliseconds to Unix time in seconds
x_unix_seconds = x_unix_millis  # Convert Unix time in milliseconds to Unix time in seconds

x_datetime = [] # Convert Unix time in seconds to datetime objects
for unix_time in x_unix_seconds:
    dt_object = datetime.datetime.fromtimestamp(unix_time)
    x_datetime.append(dt_object)

# y_compute_volt = [] #compute y from adc to mV with 0.125mV per bit
# for mv_adc in y:
#     mv_object = mv_adc*0.0078125
#     y_compute_volt.append(mv_object)

# plt.plot(y)
plt.plot(x_datetime, y)
plt.xlabel('Time')
plt.ylabel('Resistance in Ohm')
# plt.title('PID Response')
plt.show()
