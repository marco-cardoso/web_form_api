from src.database import forms

import mongomock
import unittest


class TestDatabase(unittest.TestCase):

    def setUp(self):
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

    def test_insert_form(self):
        result = forms.insert(
            self.db,
            {
                "background_colour": "234 234 234",
                "background image": "path_to_the_image",
                "height": 30,
                "background colour": "234 234 234",
                "border radius": 1,
                "body text": "Hello World"
            }
        )

        amt_docs = len(list(forms.find_all(self.db)))
        self.assertIsNotNone(result.inserted_id)
        self.assertEquals(amt_docs, 2)

    def test_get_form(self):
        result = forms.find_by_id(self.db, self.saved_form_id)
        self.assertEquals(result["background_colour"], "234 224 234")
        self.assertEquals(result["body text"], "Testing")
