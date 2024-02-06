# your User class goes here


class User:
    
    def __init__(self, first_name, email, phoneNumber, gender):
        self.first_name = first_name
        self.email = email
        self.phoneNumber = phoneNumber
        self.gender = gender

    def get_name_and_number(self):
        return f"{self.first_name}: {self.phoneNumber}"

    def __str__(self):
        return f"this user's first_name is {self.first_name}, email is {self.email}, phone number is {self.phoneNumber}, and is a {self.gender}"

    def my_decorator(func):
        def wrapper(self):
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello(self):
        print("Hello!")


p1 = User('natalie', 'rivero@mymail.com', '555-555-5555', 'female')
p2 = User('austin', 'austin@mymail.com', '333-333-3333', 'male')

print(p1.get_name_and_number())





class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Note that in the above example we have prefaced our Class attributes with an "_". 
        #This is to tell other developers that these attributes are not to pe touched 
        #and to instead utilize getters and setters to change/get this properties value.

    # THIS DOES NOT FULLY PRIVATIZE THIS ATTRIBUTE IT EXPECTS FELLOW 
        #DEVELOPERS TO UNDERSTAND THIS SYNTAX AND FOLLOW PRESCRIBED RESTRICTIONS

    # Getter for name attribute
    @property
    def get_name(self):
        return self._name

    # Setter for name attribute
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a string.")

    # Getter for age attribute
    @property
    def get_age(self):
        return self._age

    # Setter for age attribute
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive integer.")

# Create an instance of Person
person = Person("Alice", 25)

# Access and modify attributes using getters and setters
print(person.get_name)  # Output: Alice
person.set_name="Bob"
print(person.get_name)  # Output: Bob
person.set_age = 30
print(person.get_age)   # Output: 30