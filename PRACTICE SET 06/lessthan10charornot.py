Username=input("Enter Your Username: ")
B=len(Username)
if(B>10):
    print("Username Has More Than 10 Character")
elif(B<10):
    print("Username Has Less Than 10 Character")
elif(B==10):
    print("Username Has 10 Character")
input("Press Enter To Exit")