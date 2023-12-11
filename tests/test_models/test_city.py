import unittest
from models.city import City
import pep8

class TestCity(unittest.TestCase):
    def test_init(self):
        city_instance = City()
        self.assertTrue(isinstance(city_instance, City))
        self.assertTrue(isinstance(city_instance, BaseModel))
        self.assertEqual(city_instance.state_id, "")
        self.assertEqual(city_instance.name, "")
        
    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files(['models/base_model.py']),

    def test_init_with_arguments(self):
        data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'state_id': 'state123',
            'name': 'Example City'
        }
        city_instance = City(**data)
        self.assertEqual(city_instance.id, '123')
        self.assertEqual(str(city_instance.created_at), '2022-01-01 00:00:00')
        self.assertEqual(city_instance.state_id, 'state123')
        self.assertEqual(city_instance.name, 'Example City')

if __name__ == '__main__':
    unittest.main()
