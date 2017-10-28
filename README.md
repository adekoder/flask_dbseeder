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
[Example](https://gist.github.com/adekoder/8ea82a1581d801c5ca71eba4b7edaad6)

With the above application you can create the database or enable migrations if the database already exists with the following command:
> flask seed run
Note that the FLASK_APP environment variable must be set according to the Flask documentation for this command to work. 

The above command will run the seed operation, if no expection is thrown your data will be seeded into the database

###### Resources
* Documentation.

