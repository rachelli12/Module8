import unittest
from more_fun_with_collections import assign_average as aa

class TestGrade(unittest.TestCase):
    def test_average_grade_a(self):
        average = 90
        self.assertEqual(average, aa.score_to_grade())
    def test_average_grade_b(self):
        average = 80
        self.assertEqual(average, aa.score_to_grade())
    def test_average_grade_c(self):
        average = 70
        self.assertEqual(average, aa.score_to_grade())
    def test_average_grade_d(self):
        average = 60
        self.assertEqual(average, aa.score_to_grade())
    def test_average_grade_f(self):
        average = 50
        self.assertEqual(average, aa.score_to_grade())
    def test_average_invalid(self):
        with self.assertRaises(ValueError):
            aa.switch_average(101)

if __name__ == '__main__':
    unittest.main()
