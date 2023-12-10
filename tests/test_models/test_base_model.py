<<<<<<< HEAD
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
=======
#!/usr/bin/python3
""" testing files """
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime


class BaseModel_testing(unittest.TestCase):
    """ checking BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files(['models/base_model.py',
                                         'models/__init__.py',
                                         'models/engine/file_storage.py'])
        self.assertEqual(rest.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_for_base_model(unittest.TestCase):
    """ Class test for BaseModel """
    my_model = BaseModel()

    def TearDown(self):
        """ delete json file """
        del self.test

    def SetUp(self):
        """ Create instance """
        self.test = BaseModel()

    def test_attr_none(self):
        """None attribute."""
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_kwargs_constructor_2(self):
        """ check id with data """
        dictonary = {'score': 100}

        object_test = BaseModel(**dictonary)
        self.assertTrue(hasattr(object_test, 'id'))
        self.assertTrue(hasattr(object_test, 'created_at'))
        self.assertTrue(hasattr(object_test, 'updated_at'))
        self.assertTrue(hasattr(object_test, 'score'))

    def test_str(self):
        """ Test string """
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        object_test = BaseModel(**dictonary)
        out = "[{}] ({}) {}\n".format(type(object_test).__name__, object_test.id, object_test.__dict__)

    def test_to_dict(self):
        """ check dict """
        object_test = BaseModel(score=300)
        n_dict = object_test.to_dict()

        self.assertEqual(n_dict['id'], object_test.id)
        self.assertEqual(n_dict['score'], 300)
        self.assertEqual(n_dict['__class__'], 'BaseModel')
        self.assertEqual(n_dict['created_at'], object_test.created_at.isoformat())
        self.assertEqual(n_dict['updated_at'], object_test.updated_at.isoformat())

        self.assertEqual(type(n_dict['created_at']), str)
        self.assertEqual(type(n_dict['created_at']), str)

    def test_datetime(self):
        """ check datatime """
        bas1 = BaseModel()
        self.assertFalse(datetime.now() == bas1.created_at)

    def test_BaseModel(self):
        """ check attributes values in a BaseModel """

        self.my_model.name = "Holbie"
        self.my_model.my_number = 100
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def test_savefirst(self):
        """check numbers"""
        with self.assertRaises(AttributeError):
            BaseModel.save([455, 323232, 2323, 2323, 23332])

    def test_savesecond(self):
        """ check string """
        with self.assertRaises(AttributeError):
            BaseModel.save("THIS IS A TEST")

    def test_inst(self):
        """check class """
        ml = BaseModel()
        self.assertTrue(ml, BaseModel)
>>>>>>> d47aff6f217bd8a0d10a44735533f931de3e08bd
