"""
Creating library management system ...
user can register, login , add their books details... and remove book details

 --> _password : using access modifiers concept to hide password
 --> show_library : using multiple inheritance for showing the list of items added by user
 --> ISBN:  uniquely identifies your book, and facilitates the sale of your book to
            bookstores (physical and digital) and libraries.
"""

from abc import ABC, abstractmethod  # Import the ABC class and the abstractmethod decorator from the abc module

class Book:
    def __init__(self, title, author, isbn, price, is_available=True):  # using init  to initialize book attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_available = is_available

    # using getter and setter method
    def get_title(self):  # method to get title of book
        return self.title

    def set_title(self, title):
        is_available = "Available" if self.is_available else "Not Available"
        self.title = title

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPrice: Rs.{self.price}\nAvailable: {self.is_available}\n"


class Library(ABC):  # INHERITS FROM ABC CLASS
    def __init__(self, name):
        self._name = name
        self._books = []  # taking empty list to store value
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

    def remove_book(self, isbn):  # trying to use list comprehension
        removed_books = [book.title for book in self._books if book.isbn == isbn]
        if removed_books:
            self.books = [book for book in self._books if book.isbn != isbn]
            return f"{' and '.join(removed_books)} {'have' if len(removed_books) > 1 else 'has'} been removed from the library."
        return "Book not found in the library."

    def register_user(self, username, __password):  # using _password as private method
        if username not in self._users:
            self._users[username] = __password
            return f"User {username} has been registered."
        else:
            return "Username already exists. Please select any another username."

    def login(self, username, __password):
        if username in self._users and self._users[username] == __password:
            return f"Welcome, {username}!"
        else:
            return "Login failed. Please check your username and password."


# This class inherits from both Library and Book,but it will not add any new
# attributes or methods.
class ALL_DATA(Library, Book):  # Abstract Class
    @abstractmethod
    def _Data(self):  # Abstract Method
        pass


"""
# Creating an instance of the book class and concrete subclass of liabrary
book1 = Book("Book1", "Author1", "ISBN111", 20.00)
book2 = Book("Book2", "Author2", "ISBN222", 15.00)
book3 = Book("Book3", "Author3", "ISBN333", 25.00)
"""


class show_library(Library):  # multiple inheritance . It overrides the __init__ and add_book methods.
    def __init__(self, name):
        super().__init__(name)
        self._books = []  # Initialize the _books list in the subclass

    def add_book(self, book):
        self._books.append(book)
        return f"{book.get_title()} has been added to the library."

    def view_book_list(self):
        if not self._books:
            return "Books are not Available in Library"
        else:
            print("Books are available in the library:")
            print()
            for book in self._books:
                print(book)
            return ""


my_library = show_library("My Library")

username = None  # initializing the username outside the loop

while True:
    print("\nLibrary Name:", my_library._name)
    user_input = input(
        "Press 1 to register, Press 2 for login, Press 3 to add a book, Press 4 to remove a book,Press 5 for view_book_list, Press q to quit,\n Enter Your Choice: ")

    if user_input == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        registration_result = my_library.register_user(username, password)
        print(registration_result)

    elif user_input == '2':  # using exception handling
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            login_result = my_library.login(username, password)
            print(login_result)
        except Exception as e:
            print(f"An error occurred during the login: {e}")

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

    elif user_input == '5':
        books_result = my_library.view_book_list()
        print("\n", books_result)

    elif user_input == 'q':
        break
