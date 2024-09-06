#Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you can 
# print all books, add a book and get the number of books using different methods. 
# Show that your program doesn't persist the books after the program is stopped!
def intro():
        print("Welcome to the library")
        print("This is a simple library program")
        print("You can add books, print all the books and know the number of books present in this library")
        print("The books will not be saved after you exit the program")
        print("Let's start")
def end():
        print("Thank you for using this library")
        print("The program will now exit")
        exit()
class library:
        def __init__(self,book):
            self.books=[book]
            self.no_of_book=1
        def print_all_books(self):
            print(f"Books present in this library are: {[books for books in self.books]}")
        def add_a_book(self,another):
            self.books.append(another)
            self.no_of_book+=1
        def num_of_books(self):
            print(f"The number of books present in this library are: {self.no_of_book}")
intro()
book=library(input("Enter the name of the book: "))
print("Do you want to add more books? Enter 'yes' or 'no'")
choice=input()
if choice.lower() == "yes":
    for i in range(int(input("how many books do you want to enter? "))) :
        book.add_a_book(input("Enter the name of the books:  ") )
print("Do you want to print all the  books? Enter 'yes' or 'no'")
choice2=input()
if choice2.lower() == "yes":
    book.print_all_books()
print("Do you want to know the number of books present in this library? Enter 'yes' or 'no'")
choice3=input()
if choice3.lower() == "yes":
    book.num_of_books()
end()
# The Library class can be further extended to include additional functionality for managing books in a library.
# For example, methods can be added to remove books, search for books, and update book information.
# The Library class can be used as a foundation for building a library management system in Python.
# The program demonstrates the use of object-oriented programming concepts to create a Library class for managing books in a library.
