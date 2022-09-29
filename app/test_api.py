import unittest
import requests
import json


class TestApi(unittest.TestCase):
    url = "http://127.0.0.1:5000/plate"
    url_search = "http://127.0.0.1:5000/search-plate"
    data = {"plate": "B3"}

    def test_getall_car_details(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post_car_details(self):
        response = requests.post(self.url, json=self.data)
        self.assertEqual(response.status_code, 200)

    def test_search_car_details(self):
        response= requests.get(self.url,params={"key":"test","levenshtein":"9"})
        print(response.json())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
