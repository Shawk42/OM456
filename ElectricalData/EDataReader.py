import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

"""IMPORTATION"""
east = genfromtxt('EastFeed.csv',delimiter= ',')
west = genfromtxt('WestFeed.csv',delimiter=',')

"""DATA EXTRACTION"""
west_pwr = west[:,6]
east_pwr = east[:,6]

"""DATA CLEANING"""
west_pwr = np.delete(west_pwr,0)
east_pwr = np.delete(east_pwr,0)

length = len(west_pwr)

"""OUTAGE DETECTION"""

west_pwrout = np.zeros(length)

np.copyto(west_pwrout,west_pwr)
np.putmask(west_pwrout,west_pwrout>1,-1)
west_pwrout = 1+west_pwrout

east_pwrout = np.zeros(length)
np.copyto(east_pwrout,east_pwr)
np.putmask(east_pwrout,east_pwrout>1,-1)
east_pwrout = 1+east_pwrout



plt.subplots_adjust(hspace=0.4,wspace=0.4)

plt.subplot(2,2,1)
plt.plot(west_pwr)
plt.grid()
plt.title("West Feed")

plt.subplot(2,2,3)
plt.plot(east_pwr)
plt.grid()
plt.title("East Feed")

plt.subplot(2,2,2)
plt.plot(west_pwrout)
plt.grid()
plt.title("West Feed Outage")

plt.subplot(2,2,4)
plt.plot(east_pwrout)
plt.grid()
plt.title("East Feed Outage")

plt.show()
