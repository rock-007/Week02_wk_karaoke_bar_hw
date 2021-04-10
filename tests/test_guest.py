import unittest
from src.guest import Guest

class Test_guest (unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest("Adam")
        self.guest_02 = Guest("John")



    def test_guest_01_created(self):
        self.assertEqual("Adam", self.guest_01.name)

    def test_guest_02_created(self):
        self.assertEqual("John", self.guest_02.name)