import unittest
from src.guest import Guest

class Test_guest (unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest("Adam", 50, [])
        self.guest_02 = Guest("John", 35, [])



    def test_guest_01_created(self):
        self.assertEqual("Adam", self.guest_01.name)

    def test_guest_02_created(self):
        self.assertEqual("John", self.guest_02.name)

    def test_guest_01_money_in_wallet(self):
        self.assertEqual(50, self.guest_01.wallet)

    def test_guest_02_created(self):
        self.assertEqual(35, self.guest_02.wallet)