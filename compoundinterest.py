P=float(input("Enter the PRINCIPLE amount:\n"))
R=float(input("Enter the RATE of interest:\n"))
T=float(input("Enter the TIME period:\n"))
A=P*(1+R/100)**T
CI=A-P
print("The COMPOUND INTEREST according to these VALUES are:\n",CI)
