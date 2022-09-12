class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def AvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
                print("--> ", book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book Which you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book Which you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["C++", "C", "Java","Python","Django","Javascript","Web Development","Computer Graphics","Operating System","Data Structure","Algorithm","Digital Electronics","Microprocessor"])
    student = Student()
    while(True):
        welcome = '''\n ********** Welcome to Central Library **********
        Please choose an option:
        1. View The List Of all the books
        2. Request a book Which is Available in Library
        3. Return a book Which You Have Borrowed Earlier
        4. Exit From Library......
        '''
        print(welcome)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.AvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
