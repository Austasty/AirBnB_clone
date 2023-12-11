#!/usr/bin/python3
"""
Unit tests for the State class
"""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.state = State()

    def test_inheritance(self):
        """
        Test if State inherits from BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """
        Test if State has the required attributes
        """
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attributes_type(self):
        """
        Test if State attributes have the correct types
        """
        self.assertEqual(type(self.state.name), str)

    def test_str_method(self):
        """
        Test the __str__ method of State
        """
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of State
        """
        state_dict = self.state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['created_at'], self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], self.state.updated_at.isoformat())
        self.assertEqual(state_dict['name'], self.state.name)

    def test_kwargs_constructor(self):
        """
        Test the constructor of State with kwargs
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'name': 'California'
        }
        new_state = State(**data)

        self.assertEqual(new_state.id, '123')
        self.assertEqual(new_state.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_state.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_state.name, 'California')


if __name__ == '__main__':
    unittest.main()
