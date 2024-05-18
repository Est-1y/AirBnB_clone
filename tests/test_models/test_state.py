#!/usr/bin/python3
"""state unittest"""

import unittest
from models import State
from datetime import datetime
import os


class TestStateModel(unittest.TestCase):
    """State test """
    def setUp(self):
        self.state_model = State()

    def tearDown(self):
        """ """
        del self.state_model

    def test_instance_creation(self):
        """instance test """
        self.assertIsInstance(self.state_model, State)
        self.assertTrue(hasattr(self.state_model, 'id'))
        self.assertTrue(hasattr(self.state_model, 'created_at'))
        self.assertTrue(hasattr(self.state_model, 'updated_at'))
        self.assertTrue(hasattr(self.state_model, 'name'))

    def test_str(self):
        """ """
        str = str(self.state_model)
        self.assertIn("[State]", str)
        self.assertIn("id", str)
        self.assertIn("created_at", str)
        self.assertIn("updated_at", str)
        self.assertIn("name", str)

    def test_to_dict_method(self):
        state_dict = self.state_model.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)


if __name__ == '__main__':
    unittest.main()