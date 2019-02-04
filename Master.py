

"""INPUTS"""

TGT = 2            #Nominal Value
mu = "null"             #Average Value
UTL = "ans"         #Upper tolerance limit
LTL = "ans"         #Lower tolerance limit
SD = 0.001          #Standard deviation
Tol_sigma = "null"  #Tolerance range but in sigma
K = 6          #Sigma Level
CP = 1.3        #CP index
UCL = "ans"
LCL = "ans"

"""COMMON CALCS"""  #May have to comment out illegal operations
#Tol_range = UTL-LTL  #Found by dimensions
Cntrl_range = K*SD
Tolerance_range = CP*Cntrl_range   #Range that dimenions need to be in

"""EQUATION LOGIC"""
if TGT == "ans":
    "Solving for TGT"
elif mu == "ans":
    "Solving for mu"
elif UTL == "ans":
    print("Solving for UTL")
    UTL = TGT+(Tolerance_range/2)
elif LTL == "ans":
    print("Solving for LTL")
    LTL = TGT-(Tolerance_range/2)
elif SD == "ans":
    print("Solving for SD")
    SD = (Tol_range/2)*(1/K)
elif Tol_sigma == "ans":
    "Solving for Tolerance Range but in Sigma"
elif K == "ans":
    print("Solving for Sigma Level")
    K = (Tol_range/2)*(1/SD)
    print("The process operates at a",K,"Sigma Level")
elif UCL == "ans":
    print("Solving for UCL")
    UCL = TGT+(Cntrl_range/2)
elif LCL == "ans":
    print("Solving for LCL")
    LCL = TGT-(Cntrl_range/2)
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
print("LCL",LCL)
print("UCL",UCL)
print("CP ",CP)