from flask import Flask
from flask_dbseeder import Seeder
app = Flask(__name__)

seeder = Seeder(app)

if __name__ == '__main__':
    #app.run(debug=True)
    print(seeder)
