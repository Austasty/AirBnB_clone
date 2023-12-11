#!/usr/bin/python3
"""
Unit tests for the User class
"""

import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.user = User()

    def test_inheritance(self):
        """
        Test if User inherits from BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """
        Test if User has the required attributes
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_type(self):
        """
        Test if User attributes have the correct types
        """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_str_method(self):
        """
        Test the __str__ method of User
        """
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of User
        """
        user_dict = self.user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], self.user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

    def test_kwargs_constructor(self):
        """
        Test the constructor of User with kwargs
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'email': 'test@example.com',
            'password': 'secure_password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        new_user = User(**data)

        self.assertEqual(new_user.id, '123')
        self.assertEqual(new_user.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_user.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_user.email, 'test@example.com')
        self.assertEqual(new_user.password, 'secure_password')
        self.assertEqual(new_user.first_name, 'John')
        self.assertEqual(new_user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
