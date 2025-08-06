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
            self.mypost()  # Call mypost method
        elif user_input == "4":
            self.sendmsg()  # Call sendmsg method
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

    def mypost(self):
        if self.logged_in == True:
            print("You can post to other users.")
            post = input("Enter your post: ")
            print(f"Post sent: {post}")
            self.menu()


        else:
            print("Please log in to create a post.") 
            self.menu()
    
        
    def sendmsg(self):
        if self.logged_in == True:
            print("You can send messages to other users.")
            msg = input("Enter your message: ")
            print(f"Message sent: {msg}")
            self.menu()


        else:
            print("Please log in to create a post.") 
            self.menu()
            
            
# Create an instance of chatbook class
object1 = chatbook()