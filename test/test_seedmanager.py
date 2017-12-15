import unittest
from test import app, db, Seeder, SeedManager, UserSeeder, UserSeeder2, UserSeeder3, NotASubClassException


class TestSeedManager(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.seeder = Seeder(app, db)

    def tearDown(self):
        db.drop_all()

    def testIfSeedIsSubclassOfSeedManager(self):
        """ Test if seed class is a subclass of seedmanager"""
        self.seeder.add_seeds([UserSeeder])
        manager = SeedManager(app.extensions)
        with self.assertRaises(NotASubClassException) as e:
            manager.run_seeds()

    def test_if_seeds_is_not_a_class(self):
        """ Test if seed class passed is a class """
        self.seeder.add_seeds(['UserSeeder'])
        manager = SeedManager(app.extensions)
        with self.assertRaises(TypeError) as ctx:
            manager.run_seeds()

    def test_if_seeds_run_method_is_not_implemented(self):
        """ Test if seed class those not have it own run method """
        self.seeder.add_seeds([UserSeeder3])
        manager = SeedManager(app.extensions)
        with self.assertRaises(NotImplementedError) as ctx:
            manager.run_seeds()

    def test_if_no_exception_is_raised(self):
        """ Test if operation seeds successfully """
        self.seeder.add_seeds([UserSeeder2])
        manager = SeedManager(app.extensions)
        result = manager.run_seeds()
        self.assertTrue(result)
