import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

data = genfromtxt('2012Data.csv',delimiter= ',')
i = 2
temp = np.array([])
A = np.array([])
B = np.array([])
C = np.array([])
D = np.array([])

#Extracting Temperature
while i <= 2558:
    temp_line = data[i,:]
    temp_line = np.delete(temp_line, 0)
    temp_line = np.delete(temp_line, np.size(temp_line) - 1)
    temp_line = np.delete(temp_line, np.size(temp_line) - 1)
    temp = np.append(temp,temp_line)
    i = i+7

#A boiler
i = 3
while i <= 2559:
    A_line = data[i,:]
    A_line = np.delete( A_line, 0)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    A = np.append(A, A_line)
    i = i+7
#B boiler
i = 4
while i <= 2560:
    A_line = data[i,:]
    A_line = np.delete( A_line, 0)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    B = np.append(B, A_line)
    i = i+7
#C boiler
i = 5
while i <= 2561:
    A_line = data[i,:]
    A_line = np.delete( A_line, 0)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    C = np.append(C, A_line)
    i = i+7
#C boiler
i = 6
while i <= 2562:
    A_line = data[i,:]
    A_line = np.delete( A_line, 0)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    A_line = np.delete( A_line, np.size( A_line) - 1)
    D = np.append(D, A_line)
    i = i+7

A = np.nan_to_num(A)
B = np.nan_to_num(B)
C = np.nan_to_num(C)
D = np.nan_to_num(D)

master = np.stack((temp,A,B,C,D))
master = np.transpose(master)


np.savetxt('Master2012.csv',master,delimiter=',')

print("Complete")
print("First term of temp",temp.item(0))
print("First term of A",A.item(0))
print("First term of B",B.item(0))
print("First term of C",C.item(0))
print("First term of D",D.item(0))

plt.plot(temp,A,'*')
plt.xlabel("Temperature [F]")
plt.ylabel("m_dot of A [Kps]")
plt.grid()
plt.show()

