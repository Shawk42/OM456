'''
THE GOAL OF THIS CODE IS TO FOLLOW ALONG AN EXCEL DOCUMENT IN PYTHON
'''

import numpy as np
import numpy.random as rnp
from scipy import stats

"""GIVENS"""
TGT = 945
mu = TGT
Spill = 950
Fine = 942
SD = 15
Container_Cost = 3.00 #Cost for material in target size container
Spill_Cost = 1
Fine_Cost = 4
Takt = 1.75   #Takt time in seconds

"""OTHER CALCULATIONS"""
Unit_max = 1500000
Unit_min = 1100000
Units = np.round((Unit_min+(rnp.random()*(Unit_max-Unit_min))))

if Units > Unit_max:
    print("ERROR - Units is larger than Units Max")

#Units Being spilled and fined
a = np.array([0.7972])
b = stats.zscore(a)
print(b)