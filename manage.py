from app import app, db
from flask_script import Manager, Shell
from flask_dbseeder import Seeder, SeederCommand
from Seeder import UserSeeder

seeder = Seeder(app)
seeder.add_seeds([UserSeeder])

manager = Manager(app)
manager.add_command('seed', SeederCommand)

@manager.command
def create_db():
    db.create_all()

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
