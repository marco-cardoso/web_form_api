import json
from tests.utils import get_app

import unittest


class TestHealthView(unittest.TestCase):

    def setUp(self):
        app = get_app.get().test_client()
        self.response = app.get('/health')

    def test_get_status(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_response(self):
        data = self.response.data.decode('utf-8')
        self.assertEqual("ok", json.loads(data)['message'])

    def test_get_content_type(self):
        self.assertEqual("application/json", self.response.content_type)
