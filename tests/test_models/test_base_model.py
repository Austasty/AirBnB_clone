import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a new instance of BaseModel for testing."""
        self.base_model = BaseModel()

    def test_init(self):
        """Test the initialization of BaseModel."""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Test the string representation (__str__) of BaseModel."""
        expected_str = f"[{self.base_model.__class__.__name__}]({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    @patch('datetime.datetime')
    def test_save(self, mock_datetime):
        """Test the save method of BaseModel."""
        mock_datetime.today.return_value = datetime(2023, 1, 1)
        self.base_model.save()
        self.assertEqual(self.base_model.updated_at, datetime(2023, 1, 1))

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)
    
    def test_save_updates_updated_at(self):
        """Test that calling save updates the 'updated_at' attribute."""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, initial_updated_at)

    def test_to_dict_with_custom_attributes(self):
        """Test to_dict method when custom attributes are added."""
        self.base_model.custom_attr = 'test_value'
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel',
            'custom_attr': 'test_value'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_to_dict_isoformat(self):
        """Test that the 'created_at' and 'updated_at' values are in ISO format."""
        iso_created_at = self.base_model.created_at.isoformat()
        iso_updated_at = self.base_model.updated_at.isoformat()
        object_dict = self.base_model.to_dict()
        self.assertEqual(object_dict['created_at'], iso_created_at)
        self.assertEqual(object_dict['updated_at'], iso_updated_at)

    def test_to_dict_does_not_modify_object(self):
        """Test that calling to_dict does not modify the BaseModel instance."""
        initial_dict = self.base_model.__dict__.copy()
        self.base_model.to_dict()
        self.assertEqual(self.base_model.__dict__, initial_dict)

    def test_create_instance_from_dict(self):
        """Test creating a new instance from a dictionary."""
        obj_dict = {
            'id': 'custom_id',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T01:00:00',
            '__class__': 'BaseModel',
            'custom_attr': 'test_value'
        }
        new_instance = BaseModel(**obj_dict)

        # Convert the expected datetime to ISO format for comparison
        expected_created_at = '2023-01-01T00:00:00'
        expected_updated_at = '2023-01-01T01:00:00'

        self.assertEqual(new_instance.id, 'custom_id')
        self.assertEqual(new_instance.custom_attr, 'test_value')
        
        # Convert the created_at and updated_at attributes to ISO format for comparison
        self.assertEqual(new_instance.created_at.isoformat(), expected_created_at)
        self.assertEqual(new_instance.updated_at.isoformat(), expected_updated_at)


    def test_create_instance_from_empty_dict(self):
        """Test creating a new instance from an empty dictionary."""
        obj_dict = {
            '__class__': 'BaseModel'
        }
        new_instance = BaseModel(**obj_dict)

        self.assertIsNotNone(new_instance.id)
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

        self.assertEqual(new_instance.__class__.__name__, 'BaseModel')





if __name__ == '__main__':
    unittest.main()