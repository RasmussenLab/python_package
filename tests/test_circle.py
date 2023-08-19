import unittest
from mockup.mockup import Circle


class TestCircle(unittest.TestCase):
    def test_basics(self):
        x = Circle(1)
        self.assertEqual(x.radius, 1.0)
        self.assertEqual(x.diameter, 2.0)

    def test_circumference(self):
        x = Circle.from_circumference(19)
        self.assertAlmostEqual(x.radius, 19 / (2 * 3.14159))
