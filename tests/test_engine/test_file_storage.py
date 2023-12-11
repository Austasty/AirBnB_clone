#!/usr/bin/python3
"""
Unit tests for the FileStorage class
"""

import unittest
from models.base_model import BaseModel
from models.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class
    """

    def setUp(self):
        """
        Set up test environment before each test
        """
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up test environment after each test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        """
        Test the all method of FileStorage
        """
        all_objects = self.file_storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertEqual(all_objects, FileStorage._FileStorage__objects)

    def test_new_method(self):
        """
        Test the new method of FileStorage
        """
        new_instance = BaseModel()
        self.file_storage.new(new_instance)
        key = "{}.{}".format(new_instance.__class__.__name__, new_instance.id)
        self.assertTrue(key in self.file_storage.all())

    def test_save_method(self):
        """
        Test the save method of FileStorage
        """
        new_instance = BaseModel()
        self.file_storage.new(new_instance)
        self.file_storage.save()

        with open("file.json", "r") as f:
            data = json.load(f)

        key = "{}.{}".format(new_instance.__class__.__name__, new_instance.id)
        self.assertTrue(key in data)

    def test_reload_method(self):
        """
        Test the reload method of FileStorage
        """
        new_instance = BaseModel()
        self.file_storage.new(new_instance)
        self.file_storage.save()
        self.file_storage.reload()

        key = "{}.{}".format(new_instance.__class__.__name__, new_instance.id)
        self.assertTrue(key in self.file_storage.all())

    def test_import_class_method(self):
        """
        Test the import_class method of FileStorage
        """
        class_name = "BaseModel"
        imported_class = self.file_storage.import_class(class_name)
        self.assertEqual(imported_class, BaseModel)

    def test_import_class_method_with_invalid_class(self):
        """
        Test the import_class method with an invalid class
        """
        class_name = "InvalidClass"
        with self.assertRaises(ImportError):
            self.file_storage.import_class(class_name)

    def test_import_class_method_with_invalid_module(self):
        """
        Test the import_class method with an invalid module
        """
        class_name = "BaseModel"
        # Changing the module path to an invalid one
        FileStorage._FileStorage__class_modules[class_name] = "invalid_module.invalid_path"
        with self.assertRaises(ImportError):
            self.file_storage.import_class(class_name)

    def test_import_class_method_with_invalid_class_in_module(self):
        """
        Test the import_class method with an invalid class in the module
        """
        class_name = "InvalidClass"
        # Changing the module path to an existing one, but with an invalid class
        FileStorage._FileStorage__class_modules[class_name] = "models.base_model"
        with self.assertRaises(AttributeError):
            self.file_storage.import_class(class_name)


if __name__ == '__main__':
    unittest.main()
