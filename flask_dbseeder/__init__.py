from flask import current_app
import os
from .seedmanager import SeedManager

try:
    from flask_script import Manager
except ImportError:
    Manager = None

class _SeederConfig(object):
    def __init__(self, seeder):
        self.seeder = seeder
        self.seeder_path = seeder.seeder_path

class Seeder(object):

    def __init__(self, app=None, *, directory=None):
        self.directory = directory
        if self.directory is None:
            self.directory = 'Seeder'
        if app is not None:
            self.app = app
            self.init_app(self.app)
    
    def init_app(self, app):
        self.root_path = app.__dict__['root_path']
        self.seeder_path = os.path.join(self.root_path, self.directory)
        # os.mkdir(self.directory)
        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['seeder'] = _SeederConfig(self)
    
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
def hello():
    "Just say hello"
    print (current_app.extensions['seeder'].seeder_path)

@SeederCommand.command
def move():
    seeds = SeedManager(current_app.extensions['seeds'])
    seeds()



