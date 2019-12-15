import unittest
from src.spatial import in_radius


class TestInRadius(unittest.TestCase):
    def test_one_point(self):
        is_in_radius = in_radius(2, 23.283341, 42.654045, 23.285487, 42.653729)
        self.assertTrue(is_in_radius)

    def test_filter(self):
        test_points = [
            # In 2 km
            [23.285487, 42.653729, "IN1"],
            [23.283169, 42.654171, "IN2"],
            [23.281624, 42.658211, "IN3"],
            # Out or range
            [23.339732, 42.631884, "OUT1"],
            [23.238022, 42.663134, "OUT2"],
        ]

        result = filter(lambda x: in_radius(2, 23.283341, 42.654045, x[0], x[1]), test_points)
        self.assertEqual(len(list(result)), 3)


if __name__ == "__main__":
    unittest.main()
