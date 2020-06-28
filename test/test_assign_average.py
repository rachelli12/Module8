import unittest
from more_fun_with_collections import assign_average as aa

class TestGrade(unittest.TestCase):
    def test_average_grade_a(self):
        average_grade = 'A'
        self.assertEqual(average_grade, aa.switch_average(score1 = 90, score2 = 90, score3 = 90))
    def test_average_grade_b(self):
        average_grade = 'B'
        self.assertEqual(average_grade, aa.switch_average(score1 = 80, score2 = 80, score3 = 80))
    def test_average_grade_c(self):
        average_grade = 'C'
        self.assertEqual(average_grade, aa.switch_average(score1 = 70, score2 = 70, score3= 70))
    def test_average_grade_d(self):
        average_grade = 'D'
        self.assertEqual(average_grade, aa.switch_average(score1 = 60, score2 = 60, score3 = 60))
    def test_average_grade_f(self):
        average_grade = 'F'
        self.assertEqual(average_grade, aa.switch_average(score1 = 49, score2 = 49, score3 = 49))
    def test_average_invalid(self):
        with self.assertRaises(ValueError):
            aa.switch_average(score1= 101, score2= 101, score3 = 101)

if __name__ == '__main__':
    unittest.main()
