import unittest

class PersonRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        print("SetUp")

    def test_1(self):
        print("Test #1")

    def test_2(self):
        print("Test #2")

    def tearDown(self):
        print("TearDown")