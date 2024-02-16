from user_assignment import User, FreeUser, PremiumUser


#menu face
def menu_interface():
    print('------ PostBook ------')
    print("1. Add a user")
    print("2. View User's posts")
    print("3. View Everyone's posts")
    print("4. Add a post")
    print("5. Delete a post")
    print("6. Quit")


#-----------functions for choices -------


#choice 1 --add a user
def add_user():
    name = input("what's your name? ")
    email = input("what's your email? ")
    phoneNumber = input("what's your phone number? ")

    user_instance = name
    user_instance = FreeUser(name, email, phoneNumber)
    print(f'you have added {user_instance.get_name}, user number: {User.user_count}!')



#choice 2 --view a user's post
def view_user_post():
    which_user = input('which user\'s post? ')  
    if which_user in User.every_post_ever:
        print(User.every_post_ever[which_user])
    else:
        print('this person doesn\'t have any posts yet :( ')

    return which_user



#choice 3 --view everyone's post
def view_everyone_post():
    # print(f"here is everyone's posts: {User.every_post_ever}")
    User.printing_every_post()





#choice 4 --add a post
def add_a_post():
    which_user = input('who wants to add a post?  ')
    person_found = False

    for users in User.all_users:
        if which_user == users.get_name:
            person_found = True
            post = input('write away! ... ')
            users.create_post(post)
       
    if person_found == False:
            print('Person is not registered ')

     
       


# choice 5 --delete a post
def delete_a_post():
    person_found = False
    which_user = input('which user\'s post? ')  
    if which_user in User.every_post_ever:
        person_found == True
        print(User.every_post_ever[which_user])
        for users in User.all_users:
            if which_user == users.get_name:
                person_found = True
                print(User.every_post_ever[which_user])
                delete_this_post = int(input('which post number do you want to delete?  '))
                del users.postBook[delete_this_post - 1]
                print(f'here are your updated posts: {users.postBook} ')
    if person_found == False:
            print('this person doesn\'t have any posts yet :( ')
 
  

##return to main menu function
def return_to_menu_face():
    #return to main menu
    user_input = (int(input('Press 0 if you want to return to main menu, press any other number to exit app  ')))
    return user_input


##main app code

def the_app():
    user_input = 0

    while user_input == 0:
        
        menu_interface()
        choice = int((input('Enter your choice number  ')))

        match choice:
            case 1: #--add a user
                add_user()
                # user_input = return_to_menu_face()

            case 2: #--view a user's post
                view_user_post()
                # user_input = return_to_menu_face()

            case 3: # --view everyone's post
                view_everyone_post()
                # user_input = return_to_menu_face()

            case 4: #add a post
                add_a_post()
                # user_input = return_to_menu_face()

            case 5: #delete a post
                delete_a_post()
                # user_input = return_to_menu_face()
                
            case 6: ## exit app
                break




p1 = FreeUser('natalie', 'rivero@mymail.com', '555-555-5555')
p2 = PremiumUser('rey', 'austin@mymail.com', '333-333-3333')
# p1.create_post('hi this is my first post!!:)')

the_app()