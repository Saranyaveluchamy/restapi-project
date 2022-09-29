import unittest
import requests
import json


class TestApi(unittest.TestCase):
    url = "http://127.0.0.1:16521/plate"
    url_search = "http://127.0.0.1:16521/search-plate?"
    data = {"plate": "B3"}
    key = "M-D123"
    levenshtein = 5

    def test_getall_car_details(self):
        response = requests.get(self.url)
        # also check for response.. what data ur expecting in all testcases
        self.assertEqual(response.status_code, 200)

    def test_post_car_details(self):
        response = requests.post(self.url, json=self.data)
        self.assertEqual(response.status_code, 200)

    def test_search_car_details(self):
        # use params keyword argument instead of string format
        response = requests.get(
            self.url_search + 'key={}&levenshtein={}'.format(self.key, self.levenshtein))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
