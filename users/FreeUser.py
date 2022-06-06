#import class
from users.User import User
#create new class pass in parent, to inherit
class FreeUser(User):

    
    def __init__(self,name, email, address, driver_licence):
        #use comma to pass each argument
        super().__init__(name, email, address, driver_licence)
         
    #Override the add_post method for FreeUser so that an instance of FreeUser is only able to make two posts.
    #method for user to create new post that belongs to class itself(static method)
    def user_create_post(self,random_post):
        if len(self.each_user_post) < 2:
            post = random_post
            self.each_user_post.append(post)
        elif len(self.each_user_post) == 2:
            print(f"You have reached you Post limit of 2.")
            
       
# free_guy = FreeUser("Joe", "shmjoe@gmail.com", "123 fake st", "E910843")



# free_guy.user_create_post('hi')
# free_guy.user_create_post("h2")  
# free_guy.user_create_post('h3')          
       