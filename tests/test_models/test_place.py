#!/usr/bin/python3
"""place unittest """

import unittest
from models.base_model import BaseModel
from typing import List
from models import Place
from datetime import datetime
import os


class TestPlaceModel(unittest.TestCase):
    """place test """
    def setUp(self):
        self.place_model = Place()  

    def tearDown(self):
        """ """
        del self.place_model

    def test_instance_creation(self):
        """test instance """
        self.assertIsInstance(self.place_model, Place)
        self.assertTrue(hasattr(self.place_model, 'id'))
        self.assertTrue(hasattr(self.place_model, 'created_at'))
        self.assertTrue(hasattr(self.place_model, 'updated_at'))
        self.assertTrue(hasattr(self.place_model, 'city_id'))
        self.assertTrue(hasattr(self.place_model, 'user_id'))
        self.assertTrue(hasattr(self.place_model, 'name'))
        self.assertTrue(hasattr(self.place_model, 'description'))
        self.assertTrue(hasattr(self.place_model, 'number_rooms'))
        self.assertTrue(hasattr(self.place_model, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place_model, 'max_guest'))
        self.assertTrue(hasattr(self.place_model, 'price_by_night'))
        self.assertTrue(hasattr(self.place_model, 'latitude'))
        self.assertTrue(hasattr(self.place_model, 'longitude'))
        self.assertTrue(hasattr(self.place_model, 'amenity_ids'))

    def test_str(self):
        """ test string"""
        str = test_string_representation(self.place_model)
        self.assertIn("[Place]", string_repr)
        self.assertIn("id", string_repr)
        self.assertIn("created_at", string_repr)
        self.assertIn("updated_at", string_repr)
        self.assertIn("city_id", string_repr)
        self.assertIn("user_id", string_repr)
        self.assertIn("name", string_repr)
        self.assertIn("description", string_repr)
        self.assertIn("number_rooms", string_repr)
        self.assertIn("number_bathrooms", string_repr)
        self.assertIn("max_guest", string_repr)
        self.assertIn("price_by_night", string_repr)
        self.assertIn("latitude", string_repr)
        self.assertIn("longitude", string_repr)
        self.assertIn("amenity_ids", string_repr)

    def test_to_dict(self):
        """ """
        place_dict = self.place_model.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)


if __name__ == '__main__':
    unittest.main()
