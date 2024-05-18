#!/usr/bin/python3
"""Unittest """

import unittest
import os
from datetime import datetime
from models import Amenity


class test_Amenity(test_basemodel):
    """test amenity """

    def __init__(self, *args, **kwargs):
        """init function """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test name """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == '__main__':
    unittest.main()
