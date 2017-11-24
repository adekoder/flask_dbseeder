import inspect

class SeedManager(object):
    
    __not_implemeted_message = 'you must implement the run method in "%s" class'

    def __init__(self, current_app):
        self.current_app = current_app
        self.__classes = self.current_app['seeds']
        self.db = self.current_app['db']
        for klass in self.__classes:
            if not inspect.isclass(klass):
                raise TypeError("%s is a  %s a class is expected" % (klass, type(klass).__name__))
            if not issubclass(klass, SeedManager):
                raise TypeError('%s must  be a subclass of SeedManager' % klass.__name__)

    def  run(self):
        raise NotImplementedError(SeedManager.__not_implemeted_message \
            % self.__class__.__name__)

    def __call__(self):
        print('Preparing To Run seeds ')
        for klass in self.__classes:
            print('Running %s seeds' % klass.__name__)
            obj = klass(self.current_app)
            obj.run()
            print('Completed  %s seeding' % klass.__name__)
        print('Seed Operation Completed Flawlessly...')
    
    def save(self, model):
        self.db.session.add(model)
        self.db.session.commit()



