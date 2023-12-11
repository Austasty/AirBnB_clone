#!/usr/bin/python3
"""
Unit tests for the Review class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.review = Review()

    def test_inheritance(self):
        """
        Test if Review inherits from BaseModel
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """
        Test if Review has the required attributes
        """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attributes_type(self):
        """
        Test if Review attributes have the correct types
        """
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_str_method(self):
        """
        Test the __str__ method of Review
        """
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Review
        """
        review_dict = self.review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['created_at'], self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], self.review.updated_at.isoformat())
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['text'], self.review.text)

    def test_kwargs_constructor(self):
        """
        Test the constructor of Review with kwargs
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'place_id': '456',
            'user_id': '789',
            'text': 'A great place to stay!'
        }
        new_review = Review(**data)

        self.assertEqual(new_review.id, '123')
        self.assertEqual(new_review.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_review.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_review.place_id, '456')
        self.assertEqual(new_review.user_id, '789')
        self.assertEqual(new_review.text, 'A great place to stay!')


if __name__ == '__main__':
    unittest.main()
