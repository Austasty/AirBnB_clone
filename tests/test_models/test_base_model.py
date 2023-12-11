import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_type(self):
        self.assertEqual(type(self.base_model.id), str)

    def test_created_at_type(self):
        self.assertEqual(type(self.base_model.created_at), datetime)

    def test_updated_at_type(self):
        self.assertEqual(type(self.base_model.updated_at), datetime)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_kwargs_constructor(self):
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T12:34:56.789012',
            'custom_attr': 'test_value'
        }
        new_instance = BaseModel(**data)

        self.assertEqual(new_instance.id, '123')
        self.assertEqual(new_instance.created_at, datetime(2023, 1, 1))
        self.assertEqual(new_instance.updated_at, datetime(2023, 1, 2, 12, 34, 56, 789012))
        self.assertEqual(new_instance.custom_attr, 'test_value')


if __name__ == '__main__':
    unittest.main()
