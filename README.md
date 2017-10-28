# Flask-DbSeeder

Flask-DbSeeder is an extension that handles SQLAlchemy database seeds for Flask applications .
The seeding operation is provided as command line arguments for Flask-Script.

###### Installation
Install Flask-DbSeeder with pip:
''' command line
    >>> pip install Flask-DbSeeder
'''

###### Example
This is an example application that shows how to use it for more details visit the documentation page:
```python
from flask import Flask
from flask_dbseeder import Seeder, SeederCommand, SeedManager
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class UserSeeder(SeedManager):
    
    def run(self):
        user = User()
        user.username= "john"
        user.email = 'abc@gmail.com'
        self.save(user)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)
seeder = Seeder(app, db)
seeder.add_seeds([UserSeeder])
manager = Manager(app)
manager.add_command('seed', SeederCommand)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    username = db.Column(db.String(64))


if __name__ == "__main__":
    manager.run()
```

With the above application you can create the database or enable migrations if the database already exists with the following command:
> flask seed run
Note that the FLASK_APP environment variable must be set according to the Flask documentation for this command to work. 

The above command will run the seed operation, if no expection is thrown your data will be seeded into the database

###### Resources
* Documentation.

