#!/usr/bin/python3
"""
Unit tests for the Amenity class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.amenity = Amenity()

    def test_inheritance(self):
        """
        Test if Amenity inherits from BaseModel
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """
        Test if Amenity has the required attributes
        """
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attributes_type(self):
        """
        Test if Amenity attributes have the correct types
        """
        self.assertEqual(type(self.amenity.name), str)

    def test_str_method(self):
        """
        Test the __str__ method of Amenity
        """
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Amenity
        """
        amenity_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], self.amenity.name)

    def test_kwargs_constructor(self):
        """
        Test the constructor of Amenity with kwargs
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'name': 'Swimming Pool'
        }
        new_amenity = Amenity(**data)

        self.assertEqual(new_amenity.id, '123')
        self.assertEqual(new_amenity.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_amenity.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_amenity.name, 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
