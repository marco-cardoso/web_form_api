from tests.utils import get_app

import unittest


class TestHealthView(unittest.TestCase):

    def setUp(self):
        app = get_app.get().test_client()
        self.response = app.get('/health')

    def test_get_status(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_response(self):
        self.assertEqual("ok", self.response.data.decode('utf-8'))

