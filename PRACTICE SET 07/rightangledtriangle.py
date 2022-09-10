row=int(input("Enter Number Of Row: "))
for i in range(row+1):
    for j in range(i):
        print("*",end="")
    print("\r")
input("Press Enter To Exit")