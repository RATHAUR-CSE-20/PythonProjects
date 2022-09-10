from re import I


num=int(input("Enter A Number: "))
fact=1
if(num<0):
    print("Factorial Not Exist")
elif(num==0):
    print("Factorial is 1")
else:   
    for i in range(1,num+1):
        fact = fact*i
    print(f"The Factorial Of {num} is: {fact}")
input("Press Enter To Exit")