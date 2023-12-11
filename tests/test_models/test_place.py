#!/usr/bin/python3
"""
Unit tests for the Place class
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.place = Place()

    def test_inheritance(self):
        """
        Test if Place inherits from BaseModel
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """
        Test if Place has the required attributes
        """
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attributes_type(self):
        """
        Test if Place attributes have the correct types
        """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_str_method(self):
        """
        Test the __str__ method of Place
        """
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Place
        """
        place_dict = self.place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], self.place.updated_at.isoformat())
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertEqual(place_dict['user_id'], self.place.user_id)
        self.assertEqual(place_dict['name'], self.place.name)
        self.assertEqual(place_dict['description'], self.place.description)
        self.assertEqual(place_dict['number_rooms'], self.place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], self.place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], self.place.max_guest)
        self.assertEqual(place_dict['price_by_night'], self.place.price_by_night)
        self.assertEqual(place_dict['latitude'], self.place.latitude)
        self.assertEqual(place_dict['longitude'], self.place.longitude)
        self.assertEqual(place_dict['amenity_ids'], self.place.amenity_ids)

    def test_kwargs_constructor(self):
        """
        Test the constructor of Place with kwargs
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'city_id': '123',
            'user_id': '456',
            'name': 'Cozy Apartment',
            'description': 'A beautiful place to stay',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 37.7749,
            'longitude': -122.4194,
            'amenity_ids': ['1', '2', '3']
        }
        new_place = Place(**data)

        self.assertEqual(new_place.id, '123')
        self.assertEqual(new_place.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_place.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_place.city_id, '123')
        self.assertEqual(new_place.user_id, '456')
        self.assertEqual(new_place.name, 'Cozy Apartment')
        self.assertEqual(new_place.description, 'A beautiful place to stay')
        self.assertEqual(new_place.number_rooms, 2)
        self.assertEqual(new_place.number_bathrooms, 1)
        self.assertEqual(new_place.max_guest, 4)
        self.assertEqual(new_place.price_by_night, 100)
        self.assertEqual(new_place.latitude, 37.7749)
        self.assertEqual(new_place.longitude, -122.4194)
        self.assertEqual(new_place.amenity_ids, ['1', '2', '3'])


if __name__ == '__main__':
    unittest.main()
