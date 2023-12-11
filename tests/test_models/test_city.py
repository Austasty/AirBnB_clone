#!/usr/bin/python3
"""
Unit tests for the City class
"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Test cases for the City class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.city = City()

    def test_inheritance(self):
        """
        Test if City inherits from BaseModel
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Test if City has the required attributes
        """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attributes_type(self):
        """
        Test if City attributes have the correct types
        """
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)

    def test_str_method(self):
        """
        Test the __str__ method of City
        """
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of City
        """
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], self.city.updated_at.isoformat())
        self.assertEqual(city_dict['state_id'], self.city.state_id)  # Fix KeyError
        self.assertEqual(city_dict['name'], self.city.name)

    def test_kwargs_constructor(self):
        """
        Test the constructor of City with kwargs
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'state_id': 'CA',
            'name': 'San Francisco'
        }
        new_city = City(**data)

        self.assertEqual(new_city.id, '123')
        self.assertEqual(new_city.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_city.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_city.state_id, 'CA')
        self.assertEqual(new_city.name, 'San Francisco')


if __name__ == '__main__':
    unittest.main()
