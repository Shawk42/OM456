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

west_out = np.nonzero(west_pwrout)
west_out = west_out[0]
west_out = west_out-np.min(west_out)

print(west_out)
"""
After priting out the west_out variable two 
outages were found. One was 290 intervals, one was 1 interval
"""
west_outages = np.array([290,1])




east_out = np.nonzero(east_pwrout)
east_out = east_out[0]
east_out = east_out-np.min(east_out)

print(east_out)
"""
After printing the east_out variable one 
outage was found. It was 13 intervals 
"""
east_outages = np.array([13])

"""PLOTTING"""
plt.subplots_adjust(hspace=0.4,wspace=1)

plt.subplot(2,3,1)
plt.plot(west_pwr)
plt.grid()
plt.title("West Feed")

plt.subplot(2,3,4)
plt.plot(east_pwr)
plt.grid()
plt.title("East Feed")

plt.subplot(2,3,2)
plt.plot(west_pwrout)
plt.grid()
plt.title("West Feed Outage")

plt.subplot(2,3,5)
plt.plot(east_pwrout)
plt.grid()
plt.title("East Feed Outage")

plt.subplot(2,3,3)
plt.bar(np.arange(len(west_outages)),west_outages)
plt.ylabel("Outage Length [intervals]")
plt.xlabel("West Feed Outages ")

#plt.subplots_adjust((2,3,6))
#plt.bar(1,13)
#plt.ylabel("Outage Length [intervals]")
#plt.xlabel("East Feed Outages ")

plt.show()
