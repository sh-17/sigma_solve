
from abc import ABC, abstractmethod
class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPrice: Rs.{self.price}\nAvailable: {self.is_available}"

class Library(ABC): #INHERITS FROM ABC CLASS
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = {}  # Dictionary to store registered users

    @abstractmethod
    def add_book(self, book):  # Define an abstract method
        pass

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"{book.title} has been removed from the library."
        return "Book not found in the library."

    def register_user(self, username, _password):
        if username not in self.users:
            self.users[username] = _password
            return f"User {username} has been registered."
        else:
            return "Username already exists. Please choose another username."

    def login(self, username, _password):
        if username in self.users and self.users[username] == _password:
            return f"Welcome, {username}!"
        else:
            return "Login failed. Please check your username and password."

class ALL_DATA(Library, Book, ABC):  # Abstract Class
    @abstractmethod
    def __Data(self):  # Abstract Method
        pass
    print("data...................")

# Create some books and add them to the library
book1 = Book("Book1", "Author1", "ISBN111", 20.00)
book2 = Book("Book2", "Author2", "ISBN222", 15.00)
book3 = Book("Book3", "Author3", "ISBN333", 25.00)

class concreteliabrary(Library):
    def add_book(self, book):
        super().add_book(book) # Use super to call the base class method
        self.books.append(book)
        return f"{book.title} has been added to the library."

my_library = concreteliabrary("My Library")

while True:
    print("\nLibrary Name:", my_library.name)
    user_input = input("Enter Your Choice:  \n Press 1 to register:  \n Press 2 for login : \n Press 3 to add a book: \n Press 4 to remove a book: \n Press q to quit: ")

    if user_input == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        registration_result = my_library.register_user(username, password)
        print(registration_result)

    elif user_input == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_result = my_library.login(username, password)
        print(login_result)

    elif user_input == '3':
        if username in my_library.users:
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            price = float(input("Enter the price: "))
            new_book = Book(title, author, isbn, price)
            result = my_library.add_book(new_book)
            print(result)
        else:
            print("Login required to add a book.")

    elif user_input == '4':
        if username in my_library.users:
            isbn = input("Enter the ISBN of the book to remove: ")
            result = my_library.remove_book(isbn)
            print(result)
        else:
            print("Login required to remove a book.")

    elif user_input == 'q':
        break
