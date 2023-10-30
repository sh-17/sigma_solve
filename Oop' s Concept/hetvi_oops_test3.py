class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Password is private

    def change_password(self, new_password):
        self.__password = new_password
        print("Password changed successfully.")

    def login(self, password):
        return self.__password == password


class Student(User):
    def __init__(self, username, password, student_id):
        super().__init__(username, password)
        self.student_id = student_id


class Library:
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_user(self, username, password, student_id=None):
        if username not in self.users:
            if student_id is not None:
                user = Student(username, password, student_id)
            else:
                user = User(username, password)
            self.users[username] = user
            print(f"User '{username}' has been created.")
        else:
            print(f"User '{username}' already exists.")

    def add_book(self, title, price):
        self.books[title] = price
        print(f"New book added: {title}, Price: Rs.{price:.2f}")

    def list_books(self):
        print("Books in the library:")
        for title, price in self.books.items():
            print(f"{title}: Rs.{price:.2f}")


library = Library()

while True:
    print("Library Management System :")
    print("1. Register a User")
    print("2. Register a Student")
    print("3. Log In")
    print("4. Add a Book")
    print("5. List Books")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        library.add_user(username, password)
    elif choice == "2":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        student_id = input("Enter a student ID: ")
        library.add_user(username, password, student_id)
    elif choice == "3":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in library.users and library.users[username].login(password):
            print(f"Welcome, {username}!")
            while True:
                print("1. Change Password")
                print("2. List Books")
                print("3. Log Out")
                user_choice = input("Enter your choice (1/2/3): ")
                if user_choice == "1":
                    new_password = input("Enter a new password: ")
                    library.users[username].change_password(new_password)
                elif user_choice == "2":
                    library.list_books()
                elif user_choice == "3":
                    break
        else:
            print("Authentication failed. Please check your username and password.")
    elif choice == "4":
        title = input("Enter the book title: ")
        price = float(input("Enter the book price: "))
        library.add_book(title, price)
    elif choice == "5":
        print()
        library.list_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please select a valid option.")


