#!/usr/bin/python3
"""review unittest """

import unittest
from models import Review
rom models.base_model import BaseModel
from datetime import datetime
import os


class TestReviewModel(unittest.TestCase):
    """ """
    def setUp(self):
        self.review_model = Review()

    def tearDown(self):
        """ teardown"""
        del self.review_model

    def test_instance_creation(self):
        """instance test """
        self.assertIsInstance(self.review_model, Review)
        self.assertTrue(hasattr(self.review_model, 'id'))
        self.assertTrue(hasattr(self.review_model, 'created_at'))
        self.assertTrue(hasattr(self.review_model, 'updated_at'))
        self.assertTrue(hasattr(self.review_model, 'place_id'))
        self.assertTrue(hasattr(self.review_model, 'user_id'))
        self.assertTrue(hasattr(self.review_model, 'text'))

    def test_string_representation(self):
        """string test """
        string_repr = str(self.review_model)
        self.assertIn("[Review]", string_repr)
        self.assertIn("id", string_repr)
        self.assertIn("created_at", string_repr)
        self.assertIn("updated_at", str)
        self.assertIn("place_id", string_repr)
        self.assertIn("user_id", string_repr)
        self.assertIn("text", string_repr)

    def test_to_dict_method(self):
        """ dictionary test"""
        review_dict = self.review_model.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)


if __name__ == '__main__':
    unittest.main()
