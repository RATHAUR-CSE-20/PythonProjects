num = int(input('Enter Valid Number: '))
Count = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            Count = True
            break
if Count:
    print(f"{num} is Not a Prime Number")
else:
    print(f"{num} is a Prime Number")
input("Press Enter To Exit")