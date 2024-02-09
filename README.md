# App Users

You have the next big thing on the interwebs.  But a thing isn't anything without users.  In your application, users can sign up with all kinds of valuable personal information like `name`, `email address`, `driver's licence number`, you name it.

1. Write a `User` class that can handle your growing application's needs.
2. Create a few users.


#User 2---------------------------------------------------
App Users II
Wow! Literally overnight, your <INSERT APPLICATION NAME> app has really taken off! You decide to add a new feature to your app: posts.

In order to gain this new functionality, you'll have to modify your original User class.

Requirements
1.) Add a method to your User class that allows for creating a new user post.
Add any necessary instance properties to make step 1 work. What data structure should you use?
Add a static variable that stores the posts from every user. What data structure should you use?
Make sure that the the information stays in sync!
Bonus
Add a method that allows for deleting a post. Again, make sure that your information stays in sync.




#User 3---------------------------------------------------

Your User class should have several attributes and methods at this point. That's great as a general purpose representation of a user. However, as time has passed, your application's requirements have changed. You want to start making money off your app's popularity, so you've created a two-tiered system: premium users and free users.

Feel free to either start from scratch or use your (or someone else's) User class from the previous User's assignment.

Requirements
1.Your User class will now become a base class.
2 Create two subclasses PremiumUser and FreeUser that will inherit from User.
3 Override the add_post method for FreeUser so that an instance of FreeUser is only able to make two posts.
4 In the runner.py file, import FreeUser and PremiumUser and create at least one instance of each.
5 Add tests.