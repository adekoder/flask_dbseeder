from flask import Flask
from flask_dbseeder import Seeder, SeederCommand, SeedManager, NotASubClassException
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'test-db.db')
db = SQLAlchemy(app)
seeder = Seeder(app, db)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    username = db.Column(db.String(64))


class UserSeeder():

    def run(self):
        user = User()
        user.username = "john"
        user.email = 'abc@gmail.com'
        self.save(user)

class UserSeeder2(SeedManager):

    def run(self):
        user = User()
        user.username = "john"
        user.email = 'abc@gmail.com'
        self.save(user)

class UserSeeder3(SeedManager):
    pass