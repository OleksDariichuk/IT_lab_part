import unittest
from flask import Flask
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_table1_page(self):
        response = self.app.get('/table1')
        self.assertEqual(response.status_code, 200)

    def test_table2_page(self):
        response = self.app.get('/table2')
        self.assertEqual(response.status_code, 200)

    def test_product(self):
        response = self.app.post('/product')
        self.assertEqual(response.status_code, 200)

    def test_product_post(self):
        response = self.app.post('/product')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
