#!/usr/bin/python3
"""File storage testing """

import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    """storage test """
    def setUp(self):
        storage.reset()

    def tearDown(self):
        """ """
        storage.reset()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        """ all tests"""
        objects_dict = storage.all()
        self.assertIsInstance(objects_dict, dict)
        self.assertEqual(objects_dict, storage._FileStorage__objects)

    def test_new_method(self):
        """new test """
        new_object = BaseModel()
        storage.new(new_object)
        key = "{}.{}".format(new_object.__class__.__name__, new_object.id)
        self.assertIn(key, storage.all())
        self.assertEqual(
            storage.all()[key],
            new_object
        )

    def test_save_and_reload_methods(self):
        # Creating and save
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.new(obj3)
        self.file_storage.save()

        # Check created files
        self.assertTrue(os.path.exists("file.json"))

        # Clear object
        storage.reset()

        # Reload the objects
        storage.reload()

        # Check for matches in file
        key1 = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        key2 = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        key3 = "{}.{}".format(obj3.__class__.__name__, obj3.id)

        self.assertIn(key1, storage.all())
        self.assertIn(key2, storage.all())
        self.assertIn(key3, storage.all())
        self.assertEqual(
            storage.all()[key1].to_dict(),
            obj1.to_dict()
        )
        self.assertEqual(
            sstorage.all()[key2].to_dict(),
            obj2.to_dict()
        )
        self.assertEqual(
            storage.all()[key3].to_dict(),
            obj3.to_dict()
        )


if __name__ == '__main__':
    unittest.main()
