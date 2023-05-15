import datetime
import numpy as np
import matplotlib.pyplot as plt

data_path = 'data/MOX_ratio.txt'
data = np.loadtxt(data_path, delimiter=',', skiprows=1, usecols=[0])
y = data

# Plot y against the index for csv ratio file 1D
plt.plot(range(len(y)), y)
plt.xlabel('No. of Trials')
plt.ylabel('MOX Response')
plt.title('MOX Response')
plt.show()