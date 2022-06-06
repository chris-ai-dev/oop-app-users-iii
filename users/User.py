# Your User class goes here
# your improved User class goes here
from datetime import datetime

class User:
    #class attibute for allowing all the instances
    all_users_post = {}
    
    
    #constructor to initialize instance variables
    def __init__(self, name, email, address, driver_licence): #
        self.name = name
        self.email = email
        self.address = address
        self.driver_licence = driver_licence
        self.each_user_post = [] 

    def __str__(self):
        return f"I am {self.name}. My email is {self.email}. I live on {self.address} and my driver licence is {self.driver_licence}"
        
       #method for user to create new post that belongs to class itself(static method)
    def user_create_post(self,post):
        self.each_user_post.append(post)
        User.all_users_post[self.name] = self.each_user_post   