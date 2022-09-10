A=int(input("Enter Num1: "))
B=int(input("Enter Num2: "))
C=int(input("Enter Num3: "))
def Max(N1, N2, N3):
    if(N1>N3):
        return N1
    else:
        return N3

M=Max(A,B,C)
print("Greater Number is: ",M)
input("Press Enter To Exit")
