

# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # Note that in the above example we have prefaced our Class attributes with an "_". 
#         #This is to tell other developers that these attributes are not to pe touched 
#         #and to instead utilize getters and setters to change/get this properties value.

#     # THIS DOES NOT FULLY PRIVATIZE THIS ATTRIBUTE IT EXPECTS FELLOW 
#         #DEVELOPERS TO UNDERSTAND THIS SYNTAX AND FOLLOW PRESCRIBED RESTRICTIONS

#     # Getter for name attribute
#     @property
#     def get_name(self):
#         return self._name

#     # Setter for name attribute
#     @get_name.setter
#     def set_name(self, new_name):
#         if isinstance(new_name, str):
#             self._name = new_name
#         else:
#             print("Name must be a string.")

#     # Getter for age attribute
#     @property
#     def get_age(self):
#         return self._age

#     # Setter for age attribute
#     @get_age.setter
#     def set_age(self, new_age):
#         if isinstance(new_age, int) and new_age > 0:
#             self._age = new_age
#         else:
#             print("Age must be a positive integer.")

# # Create an instance of Person
# person = Person("Alice", 25)

# # Access and modify attributes using getters and setters
# print(person.get_name)  # Output: Alice
# person.set_name="Bob"
# print(person.get_name)  # Output: Bob
# person.set_age = 30
# print(person.get_age)   # Output: 30

# your User class goes here


class User:
    every_post_ever = {}
    user_count = 0
    all_users = []

    def __init__(self, name, email, phoneNumber):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.postBook = []
        self.post_counter = 1
        User.user_count += 1
        User.all_users.append(self)
        

    @property
    def get_name_and_number(self):
        return f"{self.name}: {self.phoneNumber}"
    @property
    def get_name(self):
        return self.name
    @property
    def get_email(self):
        return self.email
    @property
    def get_phoneNumber(self):
        return self.phoneNumber
    @property
    def get_postBook(self):
        return f'here are of the posts: {self.postBook}'
    
    @classmethod
    def printing_every_post(cls):
        print('HERE ARE ALL THE POSTS:')
        for user in cls.every_post_ever:
            print(f'{user}: {cls.every_post_ever[user]}')

    

    def __str__(self):
        return f"this user's name is {self.name}, email is {self.email}, phone number is {self.phoneNumber}"

    def __repr__(self):
        return f"this user's name is {self.name}, email is {self.email}, phone number is {self.phoneNumber}"


    def create_post(self, post):
        new_post = f'{self.post_counter}. {post}'
        self.postBook.append(new_post)
        User.every_post_ever[self.get_name] = self.postBook
        print('posted!')
        self.post_counter += 1
        # print(f"here are all of {self.get_name}'s posts: {User.every_post_ever[self.get_name]}")
    

    def delete_post(self, post_number_to_delete):
        del self.postBook[post_number_to_delete - 1]
        print(self.postBook)
        
        

#-----------------------------------

class FreeUser (User):
    '''can only make 2 posts'''
    
    def __init__(self, name, email, phoneNumber):
        super().__init__(name, email, phoneNumber)

    def create_post(self, post):
         if self.post_counter == 3: #self post_counter starts at 1 when instance is instantiated
             print('you\'ve already made 2 posts, please upgrade to premium')
         else:
            super().create_post(post)
         
         








# p1 = FreeUser('natalie', 'rivero@mymail.com', '555-555-5555')
# p2 = FreeUser('austin', 'austin@mymail.com', '333-333-3333')

# p1.create_post('hi this is my first post!!:)')
# print(p1.get_postBook)
# print('  ')

# p2.create_post('this MYY FIRST POST!')
# print(p2.get_postBook)
# print('    ')


# p1.create_post('second post!!')

# # User.printing_every_post()
# print(p1.get_postBook)

