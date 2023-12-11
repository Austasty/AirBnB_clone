# import unittest
# from models.amenity import Amenity
# import pep8


# class TestAmenity(unittest.TestCase):
#     def test_init(self):
#         amenity_instance = Amenity()
#         self.assertTrue(isinstance(amenity_instance, Amenity))
#         self.assertTrue(isinstance(amenity_instance, BaseModel))
#         self.assertEqual(amenity_instance.name, "")

#     def test_init_with_arguments(self):
#         data = {'id': '123', 'created_at': '2022-01-01T00:00:00', 'name': 'Example Amenity'}
#         amenity_instance = Amenity(**data)
#         self.assertEqual(amenity_instance.id, '123')
#         self.assertEqual(str(amenity_instance.created_at), '2022-01-01 00:00:00')
#         self.assertEqual(amenity_instance.name, 'Example Amenity')
#     def testpep8(self):
#         """ testing codestyle """
#         pepstylecode = pep8.StyleGuide(quiet=True)
#         rest = pepstylecode.check_files(['models/base_model.py']),
                       

# if __name__ == '__main__':
#     unittest.main()
