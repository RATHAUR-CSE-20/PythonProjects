Row = int(input("Enter the row size:"))
for i in range(Row+1):
    for j in range(Row-i):
        print(" ", end="")
    for p in range(i+1):
        print("* ", end="")
    print("\r")
input("Press Enter To Exit")