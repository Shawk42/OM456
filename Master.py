

"""INPUTS"""

TGT = 30            #Nominal Value
mu = 30             #Average Value
UTL = "ans"         #Upper tolerance limit
LTL = "ans"         #Lower tolerance limit
SD = 0.00075          #Standard deviation
Tol_sigma = "null"  #Tolerance range but in sigma
K = 4          #Sigma Level
CP = "ans"        #CP index

"""COMMON CALCS"""
Tol_range = UTL-LTL

"""EQUATION LOGIC"""
if TGT == "ans":
    "Solving for TGT"
elif mu == "ans":
    "Solving for mu"
elif UTL == "ans":
    "Solving for UTL"
elif LTL == "ans":
    "Solving for LTL"
elif SD == "ans":
    print("Solving for SD")
    SD = (Tol_range/2)*(1/K)
elif Tol_sigma == "ans":
    "Solving for Tolerance Range but in Sigma"
elif K == "ans":
    print("Solving for Sigma Level")
    K = (Tol_range/2)*(1/SD)
    print("The process operates at a",K,"Sigma Level")
elif CP == "ans":
    print("Solving for CP")
    num = UTL-LTL
    dem = K*(SD)
    CP = num/dem
    print("CP",CP)

else:
    print("No answer solved for")

print(""*50)
print("Numerical Summary")
print("TGT ",TGT)
print("mu ",mu)
print("UTL ",UTL)
print("LTL ",LTL)
print("Standard Deviation ",SD)
print("Tolerance Range in Sigma ",Tol_sigma)
print("Sigma Level ",K)
print("CP ",CP)