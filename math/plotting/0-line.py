/usr/bin/env python3
'''

This script generates data points for the x-axis ranging from 0 to 10 and computes the corresponding y-axis values by raising them to the power of 3. It then plots a line graph with a red line.
'''
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)
'''Plotting the points'''
plt.plot(x, y, 'r-')  # Plot y as a red solid line
plt.xlim(0, 10)  # Set x-axis range from 0 to 10
plt.show()
