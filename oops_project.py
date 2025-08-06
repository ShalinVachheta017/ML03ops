# Simple Chatbook class to demonstrate OOP concepts

class chatbook:
    def __init__(self):
        # Initialize user details and login status
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()  # Show menu when object is created
        print("Chatbook object created with default values")
        print("Constructor called automatically when an object is created")
        print("Welcome to Chatbook!")
        
    def menu(self):
        # Display menu options to the user
        user_input = input(" Welcome to Chatbook! How would you like to proceed?\n"
                           "1. Press 1 to sign up\n"
                           "2. Press 2 to log in\n"
                           "3. Press 3 to write post\n"
                           "4. Press 4 to message to another user\n"
                           "5. Press any key to log out(exit)\n")
        
        # Handle user input and call appropriate methods
        if user_input == "1":
            self.signup()  # Call signup method
        elif user_input == "2":
            self.signin()  # Call signin method (fixed: was 'pass')
        elif user_input == "3":
            pass  # Placeholder for write post method
        elif user_input == "4":
            pass  # Placeholder for message method
        else:
            print("Logging out...")
            exit()  # Exit the program
            
    def signup(self):
        # Collect user email and password for signup
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        print("Sign up successful!")
        self.username = email
        self.password = password
        self.logged_in = True
        self.menu()  # Show menu again after signup
        print("Signup method called manually by giving parameter")
        
    def signin(self):
        # Login functionality
        if self.username == "" and self.password == "":
            print("Please sign up first.")
            self.menu()
        else:
            uname = input("Enter your username: ")
            pwd = input("Enter your password: ")

            if uname == self.username and pwd == self.password:
                print("Sign in successful!")
                self.logged_in = True
                self.menu()
            else:
                print("Invalid username or password. Try again.\n")
                self.menu()

# Create an instance of chatbook class
object1 = chatbook()