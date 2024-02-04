class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either not available or has already been issued to someone else. Please wait until the book is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    def requestBook(self):
        book = input("Enter the name of the book you want to borrow: ")
        return book

    def returnBook(self):
        book = input("Enter the name of the book you want to return: ")
        return book


if __name__ == '__main__':
    centralLibrary = Library(["Algorithm", "Django", "CLRS", "Python Notes"])
    student = Student()

    while True:
        welcomeMsg = '''
        ===== Welcome to Central Library =====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            centralLibrary.displayAvailableBooks()
        elif choice == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
        elif choice == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
