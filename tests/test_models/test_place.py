#!/usr/bin/python3
"""place unittest """

import unittest
from tests.test_models.test_base_model import test_basemodel
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
        str = str(self.place_model)
        self.assertIn("[Place]", str)
        self.assertIn("id", str)
        self.assertIn("created_at", str)
        self.assertIn("updated_at", str)
        self.assertIn("city_id", str)
        self.assertIn("user_id", str)
        self.assertIn("name", str)
        self.assertIn("description", str)
        self.assertIn("number_rooms", str)
        self.assertIn("number_bathrooms", str)
        self.assertIn("max_guest", str)
        self.assertIn("price_by_night", str)
        self.assertIn("latitude", str)
        self.assertIn("longitude", str)
        self.assertIn("amenity_ids", str)

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
