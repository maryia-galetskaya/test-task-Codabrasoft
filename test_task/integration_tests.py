import unittest
import requests

class TestApp(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8080/api/most_popular_genres'

    def test_get_genres_with_valid_year(self):
        # Test with a valid year parameter
        response = requests.get(self.base_url, params={'year': '2021', 'row_count': 3})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
        self.assertTrue(all(['count' in d and 'genres' in d for d in data]))

    def test_get_genres_with_invalid_year(self):
        # Test with an invalid year parameter
        response = requests.get(self.base_url, params={'year': '1800', 'row_count': 5})
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(data, dict)
        self.assertIn('error', data)

    def test_get_genres_with_missing_year(self):
        # Test with a missing year parameter
        response = requests.get(self.base_url, params={'row_count': 10})
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(data, dict)
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()
