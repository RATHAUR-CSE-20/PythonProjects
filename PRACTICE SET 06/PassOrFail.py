mark1=int(input("Enter Marks Of First Subject: "))
mark2=int(input("Enter Marks Of Second Subject: "))
mark3=int(input("Enter Marks Of Third Subject: "))
percent=((mark1+mark2+mark3)*100)/300
if(mark1>=33 and mark2>=33 and mark3>=33 and percent>=40):
        print(f"You Passed and You Got {percent}%")
else:
    print(f"You Failed and You Got {percent}%")
input("Press Enter To Exit")