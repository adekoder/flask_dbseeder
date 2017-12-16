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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)

""" 
    creating an instance of the Seederclass pasing in 
    your app context and database instance.
"""
seeder = Seeder(app, db)

manager = Manager(app)
"""
    creating the command to run seeds
    with flask_migrate
"""
manager.add_command('seed', SeederCommand)

"""
    Create your seeders by subclass the SeedManager class
    with a run method.
    ==> the SeedManager class provides you with a save method for 
    save your data into the database.
"""
class UserSeeder(SeedManager):
    
    def run(self):
        user = User()
        user.username= "john"
        user.email = 'abc@gmail.com'
        self.save(user)

""" 
    Add the list of your seeder classes to the seeder obj 
    by calling a add_seeds and passing it the list of your seeders
"""
seeder.add_seeds([UserSeeder])

if __name__ == "__main__":
    manager.run()
```

> flask seed run
Note that the FLASK_APP environment variable must be set according to the Flask documentation for this command to work. 

The above command will run the seed operation, if no expection is thrown your data will be seeded into the database

> flask seed test 
Run the above method to run test

###### Resources
* Documentation.

