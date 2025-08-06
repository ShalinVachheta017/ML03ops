# Example of a simple class in Python

# Define the Employee class
class employee:
    # Constructor: runs when an object is created
    def __init__(self):
        # Instance variables (unique to each object)
        print("Constructor called automatically when an object is created")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"
        print("Employee object created with default values")
        
    # Method: action the object can perform
    def travel(self, destination):
        print(f"Employee {self.id} is travelling to {destination}")
        print("travel method called manually by giving parameter")

# Create an object (instance) of the employee class
sln = employee()

# Access and print the object's attributes
print("Employee ID:", sln.id)
print("Salary:", sln.salary)
print("Designation:", sln.designation)

# Call the object's method with different arguments
sln.travel("New York")
sln.travel("Los Angeles")