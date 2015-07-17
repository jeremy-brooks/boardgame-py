import unittest

class TestCase(unittest.TestCase):

    thing = 1

    def setUp(self):
        self.thing = 2

    def tearDown(self):
        self.thing = 1

    def test_default_size(self):
        self.assertEqual(self.thing, 2, 'should be 2')