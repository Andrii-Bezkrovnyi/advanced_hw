import unittest

from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.valid_student = Student("Andrii", "Bezkrovnyi", 22, 91.5)

    def test_valid_student_creation(self):
        self.assertEqual(self.valid_student.first_name, "Andrii")
        self.assertEqual(self.valid_student.last_name, "Bezkrovnyi")
        self.assertEqual(self.valid_student.age, 22)
        self.assertAlmostEqual(self.valid_student.average_grade, 91.5)

    def test_honors_status_true(self):
        self.assertTrue(self.valid_student.is_honors())

    def test_honors_status_false(self):
        s = Student("Olena", "Koval", 21, 70.0)
        self.assertFalse(s.is_honors())

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Student("", "Koval", 20, 85.0)

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Student("Olena", "", 20, 85.0)

    def test_invalid_age_type(self):
        with self.assertRaises(ValueError):
            Student("Olena", "Koval", "twenty", 85.0)

    def test_invalid_age_value(self):
        with self.assertRaises(ValueError):
            Student("Olena", "Koval", -5, 85.0)

    def test_invalid_grade_type(self):
        with self.assertRaises(ValueError):
            Student("Olena", "Koval", 20, "eighty")

    def test_invalid_grade_range(self):
        with self.assertRaises(ValueError):
            Student("Olena", "Koval", 20, 150)


if __name__ == "__main__":
    unittest.main()
