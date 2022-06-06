# Your PremiumUser class goes here
#import class
from users.User import User
#create new class pass in parent class User
class PremiumUser(User):
    #add constructor from User class use super()
    def __init__(self,name, email, address, driver_licence):
        # use the logic from the parent Animal class without duplicating code
        #use comma to pass each argument
        super().__init__(name, email, address, driver_licence)
    
    ######DO these people have limt lets do 10 for now    
    # def user_create_post(self, post):
    #     if len(self.each_user_post) < 10:
    #         self.each_user_post.append(post)
    #     elif len(self.each_user_post) == 10:
    #         print(f"You have reached you Post limit of 10.")        
        
    def high_status(self):
       print(f"YOU are Premium")   