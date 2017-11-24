"""
Flask-SQLite3
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-DbSeeder',
    version='0.1.dev1',
    url='http://example.com/flask-sqlite3/',
    license='BSD',
    author='ogunbiyi ibrahim',
    author_email='adwumiogunbiyi@gmail.com',
    description='''This is flask extension that help managing your
        database seeding operation in an efficient manner''',
    long_description=__doc__,
    # py_modules=['flask_dbseeder'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_dbseeder','tests*'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask','Flask-Sqlalchemy','Flask-Script'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)