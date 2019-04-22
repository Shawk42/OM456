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

west_out = np.nonzero(west_pwrout)
west_out = west_out[0]
west_out = west_out-np.min(west_out)

"""
After printing out the west_out variable two 
outages were found. One was 290 intervals, one was 1 interval
"""
west_outages = np.array([290,1]) #Outage Length in intervals
west_outages = west_outages*15   #Outage length in minutes
west_outages = west_outages/60   #Outage Length in hours



east_pwrout = np.zeros(length)
np.copyto(east_pwrout,east_pwr)
np.putmask(east_pwrout,east_pwrout>1,-1)
east_pwrout = 1+east_pwrout

east_out = np.nonzero(east_pwrout)
east_out = east_out[0]
east_out = east_out-np.min(east_out)


"""
After printing the east_out variable one 
outage was found. It was 13 intervals 
"""
east_outages = np.array([13])
east_outages = east_outages*15
east_outages = east_outages/60

time = np.linspace(0,length*15,length)
time = time/60

"""Memory Size"""
mem = time.nbytes+west_pwr.nbytes+east_pwr.nbytes+west_pwrout.nbytes+east_pwrout.nbytes
mem = mem/(1*(10**9))

print("Memory Usage of graphed arrays",mem)


"""PLOTTING"""
plt.subplots_adjust(hspace=0.4,wspace=0.5)

plt.subplot(2,3,1)
plt.plot(time,west_pwr)
plt.grid()
plt.title("West Feed")
plt.xlabel("Time [hrs]")

plt.subplot(2,3,4)
plt.plot(time,east_pwr)
plt.grid()
plt.title("East Feed")
plt.xlabel("Time [hrs]")

plt.subplot(2,3,2)
plt.plot(time,west_pwrout)
plt.grid()
plt.title("West Feed Outage")
plt.xlabel("Time [hrs]")

plt.subplot(2,3,5)
plt.plot(time,east_pwrout)
plt.grid()
plt.title("East Feed Outage")
plt.xlabel("Time [hrs]")

#Bar Plots

plt.subplot(2,3,3)
plt.bar(np.arange(len(west_outages)),west_outages)
plt.ylabel("Outage Length [hrs]")
plt.title("West Feed Outages ")

plt.subplot(2,3,6)
plt.bar(1,east_outages)
plt.ylabel("Outage Length [hrs]")
plt.title("East Feed Outages ")

plt.suptitle("East and West Feed data for 2016-18")

plt.show()
