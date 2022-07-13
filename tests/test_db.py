import unittest
import os
os.environ['TESTING'] = 'true'
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# Create in-memory sqlite to run tests
test_db = SqliteDatabase(':memory:')


# TimelinePost unit test class
class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind models to test db
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Destroy the db
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts
        test_post_1 = TimelinePost.create(name="Test Poster 1", email="Tester1@example.com", content="Hello! Test #1!")
        # Make sure first created post has an ID of 1
        assert test_post_1.id == 1

        # Do same for a second post
        test_post_2 = TimelinePost.create(name="Test Poster 2", email="Tester2@example.com", content="Hello! Test #2!")
        assert test_post_2.id == 2

