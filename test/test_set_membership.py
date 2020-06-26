import unittest
import unittest.mock as mock
from more_fun_with_collections import set_membership as sm

class TestSet(unittest.TestCase):
    def test_in_set_true(self):
        #creat a set
        #assertTrue expect True to be result
        #assertTrue(sm.inset(parameter1, parameter2))
        self.assertTrue(sm.in_set())
    def test_in_set_false(self):
        self.assertFalse(sm.in_set())

if __name__ == '__main__':
    unittest.main()
