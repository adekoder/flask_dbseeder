from flask_dbseeder import SeedManager
from  app import db, User

class UserSeeder(SeedManager):
    
    def run(self):    
        user = User()
        user.email = "ma@gmail.com"
        user.username = 'ma'
        self.save(user)

        user2 = User()
        user2.email = "ad@gmail.com"
        user2.name = 'ad'
        self.save(user2)

        user3 = User()
        user.email = "sn@gmail.com"
        user.username = 'sn'
        self.save(user2)
