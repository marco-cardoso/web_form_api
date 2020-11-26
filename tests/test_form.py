from src.database import forms
from tests.utils import get_app

import mongomock
import unittest


class TestFormsView(unittest.TestCase):

    def setUp(self):
        self.app = get_app.get().test_client()
        self.db = mongomock.MongoClient().db

        form = forms.insert(
            self.db,
            {
                "background_colour": "234 224 234",
                "background image": "path_tttt_the_image",
                "height": 30,
                "background colour": "234 2311 234",
                "border radius": 1,
                "body text": "Testing"
            }
        )

        self.saved_form_id = form.inserted_id

    def test_post(self):
        form = {
            "background_colour": "234 224 234",
            "background image": "path_tttt_the_image",
            "height": 30,
            "background colour": "234 2311 234",
            "border radius": 1,
            "body text": "Testing"
        }
        response = self.app.post("/data", json=form)
        print(response)
        self.assertEquals(response.status_code, 201)

    def test_get(self):
        pass
