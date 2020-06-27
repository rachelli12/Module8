"""
Program name: test_date_time.py
Author: Rachel Li
Last date modified: 06/27/2020

The purpose of this program is to test date_time.py
"""
import datetime
import unittest
from more_fun_with_collections import date_time as dt

class TestDate(unittest.TestCase):
    def test_half_birthday(self):
        birthdate = '2020-09-24'
        expected_date = '2021-03-26'
        self.assertEqual(expected_date, dt.half_birthday(birthdate))

if __name__ == '__main__':
    unittest.main()
