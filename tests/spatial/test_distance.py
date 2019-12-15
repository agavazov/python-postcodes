import unittest
from src.spatial import points_distance


class TestDistance(unittest.TestCase):
    def test_points_in_london(self):
        # two points in London at a distance of ~20 km
        distance = points_distance(-0.223827, 51.559305, 0.066624, 51.557170)
        self.assertTrue(20 <= distance <= 20.5)

    def test_bulgaria_length(self):
        # the approximate length of Bulgaria ~450km
        distance = points_distance(22.442572, 42.817802, 27.963402, 42.819649)
        self.assertTrue(450 <= distance <= 451)


if __name__ == "__main__":
    unittest.main()
