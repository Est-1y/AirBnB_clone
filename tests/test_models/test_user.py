#!/usr/bin/python3
"""user unittest """

import os
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from time import sleep
from datetime import datetime


class TestUserModel(unittest.TestCase):
    """user model test """
    def setUp(self):
        self.user_model = User()
        self.user_model.email = "user@example.com"
        self.user_model.password = "password123"
        self.user_model.first_name = "Esther"
        self.user_model.last_name = "Obongo"

    def tearDown(self):
        del self.user_model

    def test_instance_creation(self):
        """instance test """
        self.assertIsInstance(self.user_model, User)
        self.assertTrue(hasattr(self.user_model, 'id'))
        self.assertTrue(hasattr(self.user_model, 'created_at'))
        self.assertTrue(hasattr(self.user_model, 'updated_at'))
        self.assertTrue(hasattr(self.user_model, 'email'))
        self.assertTrue(hasattr(self.user_model, 'password'))
        self.assertTrue(hasattr(self.user_model, 'first_name'))
        self.assertTrue(hasattr(self.user_model, 'last_name'))

    def test_string_representation(self):
        """string test """
        string_repr = str(self.user_model)
        self.assertIn("[User]", string_repr)
        self.assertIn("id", string_repr)
        self.assertIn("created_at", string_repr)
        self.assertIn("updated_at", string_repr)
        self.assertIn("email", string_repr)
        self.assertIn("password", string_repr)
        self.assertIn("first_name", string_repr)
        self.assertIn("last_name", string_repr)

    def test_to_dict_method(self):
        """ """
        user_dict = self.user_model.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)


if __name__ == '__main__':
    unittest.main()
