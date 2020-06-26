import unittest
import unittest.mock as mock
from more_fun_with_collections import dict_membership as dm

class TestDict(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(dm.in_dict())
    def test_in_dict_flase(self):
        self.assertFalse(dm.in_dict())

if __name__ == '__main__':
    unittest.main()
