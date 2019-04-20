import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from tempfile import TemporaryFile
outfile = TemporaryFile()

"""IMPORTATION"""
print("STATUS - Starting import")
east = genfromtxt('EastFeed.csv',delimiter= ',')
print("STATUS - East Feed Imported")
west = genfromtxt('WestFeed.csv',delimiter=',')
print("STATUS - West Feed Imported")

print("STAUS - Data Importation Complete")

"""DATA EXTRACTION"""
print("STATUS - Data Extraction Started")

west_pwr = west[:,6]
east_pwr = east[:,6]
#time = east[:,2]


print("STATUS - Data Extraction Complete")

"""DATA FILTERING"""
print("STATUS - Data Cleaning Started")
west_pwr = np.delete(west_pwr,0)
east_pwr = np.delete(east_pwr,0)

print("STATUS - Data Cleaning Complete")





length = len(west_pwr)
time = np.linspace(0,length,length)

plt.subplots_adjust(hspace=0.4)

plt.subplot(2,2,1)
plt.plot(west_pwr)
plt.grid()
plt.title("West Feed")

plt.subplot(2,2,3)
plt.plot(east_pwr)
plt.grid()
plt.title("East Feed")



plt.show()
