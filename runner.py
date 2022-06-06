# Import and create your users here
from users.User import User
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

#create instance of new user
joe = User("Jeo",'ran@gmail.com','123 fake st', 'E3421313')
#print(joe)
#I am Jeo. My email is ran@gmail.com. I live on 123 fake st and my driver licence is E3421313


#create instance of free user
free_guy = FreeUser("Sam", "shmjoe@gmail.com", "32 fake st", "E910843")
free_guy.user_create_post('hi')
free_guy.user_create_post("h2")
# print(free_guy.each_user_post)  
free_guy.user_create_post('h3')  
# ['hi', 'h2']
# You have reached you Post limit of 2.

#create instance of Premium user
premium_guy = PremiumUser("Phil", "1philloe@gmail.com", "200 hat st", "A910843")
# premium_guy.high_status()
#YOU are Premium

premium_guy.user_create_post(1)
premium_guy.user_create_post(2)
premium_guy.user_create_post(3)
print(User.all_users_post)