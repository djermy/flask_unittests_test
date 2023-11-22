import unittest
from app.application import create_app

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
    

    def test_double_endpoint(self):
        response = self.client.get('/double/5')
        result = response.get_json()
        
        self.assertEqual(result['value'], 10.0)
        self.assertEqual(200, response.status_code)

    def test_half_endpoint(self):
        response = self.client.get('/half/5')
        result = response.get_json()
        
        self.assertEqual(result['value'], 2.5)
        self.assertEqual(200, response.status_code)
    
    def test_power_of_x_endpoint(self):
        response = self.client.get('/power_of_10/5')
        result = response.get_json()

        self.assertEqual(result['value'], 9765625.0)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()