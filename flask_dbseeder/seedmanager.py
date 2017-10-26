import inspect

class SeedManager(object):
    
    __not_implemeted_message = 'you must implement the run method in "%s" class'

    def __init__(self, args=[]):
        self.__classes = args
        for klass in self.__classes:
            if not inspect.isclass(klass):
                raise TypeError("%s is a  %s a class is expected" % (klass, type(klass).__name__))
            if SeedManager not in klass.__bases__:
                raise TypeError('%s must  be a subclass of SeedManager' % klass.__name__)

    def  run(self):
        raise NotImplementedError(SeedManager.__not_implemeted_message \
            % self.__class__.__name__)

    def __call__(self):
        print('preparing to seed ')
        for klass in self.__classes:
            obj = klass()
            obj.run()
        print('database seeded')

if __name__ == "__main__":
    class User:
        name = 'james'

    class seed(SeedManager):

        def run(self):
            print('from seed')

    class seed2(SeedManager):
        
        def run(self):
            print('from seed 2')

    ''' class seed3(SeedManager):
        pass '''

    seeds = SeedManager(seed, seed2)
    seeds()
