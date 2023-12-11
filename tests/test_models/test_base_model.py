import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_create_instance(self):
        """
        Test creating an instance of BaseModel.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_generation(self):
        """
        Test the generation of unique IDs.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_string_representation(self):
        """
        Test the string representation of
        the BaseModel instance.
        """
        obj = BaseModel()
        expected_str = f"[BaseModel]({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """
        Test the save method to update the 'updated_at' attribute.
        """
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method to ensure proper dictionary format.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_to_dict_with_custom_attribute(self):
        """
        Test to_dict method with a custom attribute.
        """
        obj = BaseModel(custom_attr="test")
        obj_dict = obj.to_dict()
        self.assertIn("custom_attr", obj_dict)
        self.assertEqual(obj_dict["custom_attr"], "test")

    def test_initialize_with_custom_dates(self):
        """
        Test initialization with custom created_at and updated_at dates.
        """
        custom_created_at = "2023-01-01T12:00:00.000000"
        custom_updated_at = "2023-02-01T12:30:00.000000"
        obj = BaseModel(created_at=custom_created_at, updated_at=custom_updated_at)
        self.assertEqual(obj.created_at.isoformat(), custom_created_at)
        self.assertEqual(obj.updated_at.isoformat(), custom_updated_at)

    def test_save_after_init_with_custom_dates(self):
        """
        Test save method after initialization with custom dates.
        """
        custom_created_at = "2023-01-01T12:00:00.000000"
        obj = BaseModel(created_at=custom_created_at)
        original_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, original_updated_at)

    def test_initialize_with_invalid_date_format(self):
        """
        Test initialization with an invalid date format.
        """
        invalid_date_format = "2023/01/01 12:00:00"
        with self.assertRaises(ValueError):
            BaseModel(created_at=invalid_date_format)

    def test_initialize_with_unknown_keyword_argument(self):
        """
        Test initialization with an unknown keyword argument.
        """
        with self.assertRaises(TypeError) as context:
            BaseModel(unknown_attr="test")

        # Check that the correct exception was raised
        self.assertEqual(str(context.exception),
                         "BaseModel() got an unexpected\
                         keyword argument 'unknown_attr'")

    def test_save_after_update_object_attributes(self):
        """
        Test save method after updating object attributes.
        """
        obj = BaseModel()
        obj.custom_attr = "test"
        original_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, original_updated_at)

    def test_save_after_remove_object_attribute(self):
        """
        Test save method after removing object attribute.
        """
        obj = BaseModel()
        obj.custom_attr = "test"
        original_updated_at = obj.updated_at
        del obj.custom_attr
        obj.save()
        self.assertGreater(obj.updated_at, original_updated_at)

    def test_save_after_change_object_attribute(self):
        """
        Test save method after changing object attribute.
        """
        obj = BaseModel()
        obj.custom_attr = "test"
        original_updated_at = obj.updated_at
        obj.custom_attr = "new_value"
        obj.save()
        self.assertGreater(obj.updated_at, original_updated_at)

    def test_initialize_and_to_dict_with_all_attributes(self):
        """
        Test initialization and to_dict method with all attributes.
        """
        custom_created_at = "2023-01-01T12:00:00.000000"
        custom_updated_at = "2023-02-01T12:30:00.000000"
        obj = BaseModel(
            custom_attr="test",
            created_at=custom_created_at,
            updated_at=custom_updated_at
        )
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["custom_attr"], "test")
        self.assertEqual(obj_dict["created_at"], custom_created_at)
        self.assertEqual(obj_dict["updated_at"], custom_updated_at)

    def test_save_after_init_with_all_attributes(self):
        """
        Test save method after initialization with all attributes.
        """
        custom_created_at = "2023-01-01T12:00:00.000000"
        custom_updated_at = "2023-02-01T12:30:00.000000"
        obj = BaseModel(
            custom_attr="test",
            created_at=custom_created_at,
            updated_at=custom_updated_at
        )
        original_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, original_updated_at)


if __name__ == '__main__':
    unittest.main()
