li=[10,20,30,40,50,60,70,80,90,100]
print("Your List is\n",li)
search=int(input("Enter integer Which You Want to Search: "))
if(search==li[0] or search==li[1] or search==li[2] or search==li[3] or search==li[4] or search==li[5] or search==li[6] or search==li[7] or search==li[8] or search==li[9]):
    print("Element Found")
else:
    print("Element Not Found")
input("Press Enter To Exit")