class chatbook:
    def __init__(self):
        
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()
        print("Chatbook object created with default values")
        print("Constructor called automatically when an object is created")
        print("Welcome to Chatbook!")
        
        
    def menu(self):
        user_input = input(" Welcome to Chatbook! How would you like to proceed?\n"
                           "1. Press 1 to sign up\n"
                           "2. Press 2 to log in\n"
                           "3. Press 3 to write post\n"
                           "4. Press 4 to message to another user\n"
                           "5. Press any key to log out(exit)\n")
        
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Logging out...")
            exit()
            
    
    
object1 = chatbook()