#!/usr/bin/python3
"""city unittest """

import unittest
from datetime import datetime
import os
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """city test """

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """state id unittest """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """name unittest """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == '__main__':
    unittest.main()
