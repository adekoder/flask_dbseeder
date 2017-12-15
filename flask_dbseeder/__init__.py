from flask import current_app
from .seedmanager import SeedManager, NotASubClassException
from sqlalchemy.exc import SQLAlchemyError

try:
    from flask_script import Manager
except ImportError:
    Manager = None


class Seeder(object):

    def __init__(self, app=None, db=None):
        if app is not None and db is not None:
            self.app = app
            self.db = db
            self.init_app(self.app, self.db)

    def init_app(self, app, db):
        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['db'] = db

    def add_seeds(self, seeds=[]):
        self.seeds = seeds
        self.app.extensions['seeds'] = self.seeds


if Manager is not None:
    SeederCommand = Manager(usage="for seedding database file")
else:
    class FakeCommand(object):
        def option(self, *args, **kwargs):
            def decorator(f):
                return f
            return decorator

    SeederCommand = FakeCommand()


@SeederCommand.command
def run():
    """ This command run the database seeding process."""
    seeds = SeedManager(current_app.extensions)
    try:
        seeds.run_seeds()
    except SQLAlchemyError:
        import sys
        print('%s' % sys.exc_info())


@SeederCommand.command
def test():
    """ This command is run the test"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=3).run(tests)
