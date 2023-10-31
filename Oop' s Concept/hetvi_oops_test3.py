from abc import ABC, abstractmethod  # Import the ABC class and the abstractmethod decorator from the abc module

from setuptools.extension import Library


class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_available = True

    def get_title(self):
        return self.title  # Use the correct attribute name

    def set_title(self, title):
        self.title = title  # Use the correct attribute name

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPrice: Rs.{self.price}\nAvailable: {self.is_available}"

class Library(ABC):  # INHERITS FROM ABC CLASS
    def __init__(self, name):
        self._name = name
        self._books = []
        self._users = {}  # Dictionary to store registered users

    @abstractmethod
    def add_book(self, book):
        pass

    """def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"{book.title} has been removed from the library."
        return "Book not found in the library."""

    def remove_book(self, isbn): # trying to use list comprehension
        removed_books = [book.title for book in self._books if book.isbn == isbn]
        if removed_books:
            self.books = [book for book in self._books if book.isbn != isbn]
            return f"{' and '.join(removed_books)} {'have' if len(removed_books) > 1 else 'has'} been removed from the library."
        return "Book not found in the library."

    def register_user(self, username, _password): # using _password as private method
        if username not in self._users:
            self._users[username] = _password
            return f"User {username} has been registered."
        else:
            return "Username already exists. Please select any another username."

    def login(self, username, _password):
        if username in self._users and self._users[username] == _password:
            return f"Welcome, {username}!"
        else:
            return "Login failed. Please check your username and password."


# This class inherits from both Library and Book,but it will not add any new
# attributes or methods.
class ALL_DATA(Library, Book, ABC):  # Abstract Class
    @abstractmethod
    def __Data(self):  # Abstract Method
        pass
    print("data...................")
"""

# Creating an instance of the book class and concrete subclass of liabrary
book1 = Book("Book1", "Author1", "ISBN111", 20.00)
book2 = Book("Book2", "Author2", "ISBN222", 15.00)
book3 = Book("Book3", "Author3", "ISBN333", 25.00)

"""


class show_liabrary(Library):
    def add_book(self, book):
        super().add_book(book)  # Use super to call the base class method
        self._books.append(book)  # Use the correct attribute name
        return f"{book.get_title()} has been added to the library."


my_library = show_liabrary("My Library")

username = None  # Initialize username outside the loop

while True:
    print("\nLibrary Name:", my_library._name)
    user_input = input("Press 1 to register, Press 2 for login, Press 3 to add a book, Press 4 to remove a book, Press q to quit,\n Enter Your Choice: ")

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
        if username in my_library._users:
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            price = float(input("Enter the price: "))
            new_book = Book(title, author, isbn, price)
            result = my_library.add_book(new_book)
            print()
            print(result)
            print(new_book)

        else:
            print("Login required to add a book.")

    elif user_input == '4':
        if username in my_library._users:
            isbn = input("Enter the ISBN of the book to remove: ")
            result = my_library.remove_book(isbn)
            print(result)
        else:
            print("Login required to remove a book.")

    elif user_input == 'q':
        break