row=int(input("Enter Number Of Row:"))
print_control_x=row//2+1
for i in range(1,row+1):
    for inn in range(1,row+1):
        if (inn==1 or inn==row) or (i==1 or i==row):
            print("*",end="")
        else:
            print(" ", end="")
    print("\r")
input("Press Enter To Exit")