import datetime
import unittest
from more_fun_with_collections import date_time as dt

class TestDate(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(dt.half_birthday(2020, 9, 9), 2021, 3, 26)

if __name__ == '__main__':
    unittest.main()
