from oops_project import chatbook



# lst1 = [1, 2, 3, 4, 5]

# a1 = len(lst1)
# print(f"Length of lst1 is: {a1}")



user1 = chatbook()
# user1.sendmsg()
# print("You can send a message to another user.")
#print(f"User name is: {user1._chatbook__name}")  # Accessing private attribute with single underscore
# print(f"User name is: {user1.__name}")  # This will raise an AttributeError because __name is private attribute


# ''' Accessing and modifying private attribute using getter and setter methods'''
# print(user1.get_name())  # Accessing private attribute using getter method
# user1.set_name("New Chatbook User")  # Modifying private attribute using setter method
# print(user1.get_name())  

print(user1.id)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)