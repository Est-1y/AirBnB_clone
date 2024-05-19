#!/usr/bin/python3

"""Unittest"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class test_basemodel(unittest.TestCase):
    """basemodel unittest """
    def setUp(self):
        pass

    def tearDown(self):
        """ """
        del self.base_model

def test_instance_creation(self):
        """ Instance creation and updation"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_string_representation(self):
        """string unittest """
        string_repr = str(self.base_model)
        self.assertIn("[BaseModel]", string_repr)
        self.assertIn("id", string_repr)
        self.assertIn("created_at", string_repr)
        self.assertIn("updated_at", string_repr)

    def test_save(self):
        """test unittest"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

if __name__ == '__main__':
    unittest.main()
