# your User class goes here


class User:
    
    def __init__(self, first_name, email, phoneNumber, gender):
        self.first_name = first_name
        self.email = email
        self.phoneNumber = phoneNumber
        self.gender = gender

    def __str__(self):
        return f"this user's first_name is {self.first_name}, email is {self.email}, phone number is {self.phoneNumber}, and is a {self.gender}"

p1 = User('natalie', 'rivero@mymail.com', '555-555-5555', 'female')
p2 = User('austin', 'austin@mymail.com', '333-333-3333', 'male')

print(p1.__str__())