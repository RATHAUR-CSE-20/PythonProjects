num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter Third Number: "))
num4=int(input("Enter Fourth Number: "))
if (num1>num2):
    if (num1>num3):
        if (num1>num4):
            print(f"{num1} is Greatest")
elif(num2>num1):
    if(num2>num3):
        if(num2>num4):
            print(f"{num2} is Greatest")
elif(num3>num1):
    if(num3>num2):
        if(num3>num4):
            print(f"{num3} is Greatest")
elif(num4>num1):
    if(num4>num2):
        if(num4>num3):
            print(f"{num4} is Greatest")
elif(num1==num2 and num2==num3 and num3==num4):
    print(f"{num1},{num2},{num3} and {num4} are Equal")
input("Press Enter To Exit")

