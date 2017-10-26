from flask_dbseeder import SeedManager
from  app import db, User

class UserSeeder(SeedManager):
    
    def run(self):    
        user = User()
        user.email = "example@abc.com"
        user.username = 'john'
        db.session.add(user)
        db.session.commit()