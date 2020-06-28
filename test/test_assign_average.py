import unittest
from more_fun_with_collections import assign_average as aa

class TestGrade(unittest.TestCase):
    def test_average_grade_a(self):
        average = 90
        self.assertEqual(average, aa.switch_average(score1 = 90, score2 = 90, score3 = 90))
    def test_average_grade_b(self):
        average = 80
        self.assertEqual(average, aa.switch_average(score1 = 80, score2 = 80, score3 = 80))
    def test_average_grade_c(self):
        average = 70
        self.assertEqual(average, aa.switch_average(score1 = 70, score2 = 70, score3= 70))
    def test_average_grade_d(self):
        average = 60
        self.assertEqual(average, aa.switch_average(score1 = 60, score2 = 60, score3 = 60))
    def test_average_grade_f(self):
        average = 50
        self.assertEqual(average, aa.switch_average(score1 = 50, score2 = 50, score3 = 50))
    def test_average_invalid(self):
        with self.assertRaises(ValueError):
            aa.switch_average(101)

if __name__ == '__main__':
    unittest.main()
