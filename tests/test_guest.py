import unittest
from src.guest import Guest

class Test_guest (unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest("Umair", 70, ["Wagon Wheel"])
        self.guest_02 = Guest("John", 35, [])





# Guest_object_testings
    def test_guest_01_created(self):
        self.assertEqual("Umair", self.guest_01.name)

    def test_guest_02_created(self):
        self.assertEqual("John", self.guest_02.name)

# Guest_wallet_testing
    def test_guest_01_money_in_wallet(self):
        self.assertEqual(70, self.guest_01.wallet)

