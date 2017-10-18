"""
Flask-SQLite3
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-DbSeeder',
    version='1.0',
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
    packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'Mako'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)