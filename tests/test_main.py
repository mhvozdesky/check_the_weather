import unittest
import os
from coordinates import get_coordinates


class TestMain(unittest.TestCase):
    def test_get_coordinates(self):
        os.environ["LATITUDE"] = "40.1"
        os.environ["LONGITUDE"] = "30.1"

        coordinates = get_coordinates()

        self.assertEqual(coordinates.latitude, '40.1')
        self.assertEqual(coordinates.longitude, '30.1')


if __name__ == '__main__':
    unittest.main()
