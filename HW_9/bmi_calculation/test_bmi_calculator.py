import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_normal_weight(self):
        self.assertIn("normal", calculate_bmi(180, 75))

    def test_underweight(self):
        self.assertIn("underweight", calculate_bmi(170, 50))

    def test_overweight(self):
        self.assertIn("watch your figure", calculate_bmi(160, 80))

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)

    def test_negative_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(180, -10)

    def test_non_numeric_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi("one-seventy", 60)

    def test_non_numeric_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(170, "sixty")

    def test_boundary_low(self):
        msg = calculate_bmi(180, 59.9)
        self.assertIn("underweight", msg)

    def test_boundary_high(self):
        msg = calculate_bmi(180, 81)
        self.assertIn("watch your figure", msg)

    def test_valid_result_format(self):
        msg = calculate_bmi(180, 75)
        self.assertRegex(msg, r"Your BMI: \d+\.\d{2}")

if __name__ == "__main__":
    unittest.main()
