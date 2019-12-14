import unittest
from src.stores import Store


class TestCode(unittest.TestCase):
    def test_init_set(self):
        test_postcode = "SN25 2EG"

        # Init the class
        postcode = Store(postcode=test_postcode, name="Shop")

        # Check assertion
        self.assertEqual(postcode.postcode, test_postcode)

    def test_init_required_param(self):
        # Expect type error
        with self.assertRaises(TypeError):
            Store(name="Shop")

    def test_setter_update(self):
        test_postcode = "SN25 XXX"

        # Init the class
        postcode = Store(postcode="SN25 2EG", name="Shop")
        postcode.postcode = test_postcode

        # Check assertion
        self.assertEqual(postcode.postcode, test_postcode)

    def test_postcode_type_init(self):
        # Exception constructor TypeError
        with self.assertRaises(TypeError):
            Store(postcode=1234, name="Shop")

    def test_postcode_type_setter(self):
        # Init setter TypeError
        postcode = Store(postcode="SN25 2EG", name="Shop")

        # Expect type error
        with self.assertRaises(TypeError):
            postcode.postcode = 1234

    def test_postcode_length(self):
        # Expect constructor ValueError
        with self.assertRaises(ValueError):
            Store(postcode="", name="Shop")


class TestName(unittest.TestCase):
    def test_init_set(self):
        test_name = "Some Name"

        # Init the class
        postcode = Store(postcode="SN25 2EG", name=test_name)

        # Check assertion
        self.assertEqual(postcode.name, test_name)

    def test_init_required_param(self):
        # Expect type error
        with self.assertRaises(TypeError):
            Store(postcode="SN25 2EG")

    def test_setter_update(self):
        test_name = "Some Name"

        # Init the class
        postcode = Store(postcode="SN25 2EG", name=test_name)
        postcode.name = test_name

        # Check assertion
        self.assertEqual(postcode.name, test_name)

    def test_name_type_init(self):
        # Exception constructor TypeError
        with self.assertRaises(TypeError):
            Store(postcode="SN25 2EG", name=1234)

    def test_name_type_setter(self):
        # Init setter TypeError
        postcode = Store(postcode="SN25 2EG", name="Shop")

        # Expect type error
        with self.assertRaises(TypeError):
            postcode.name = 1234

    def test_name_length(self):
        # Expect constructor ValueError
        with self.assertRaises(ValueError):
            Store(postcode="SN25 2EG", name="")


class TestLongitude(unittest.TestCase):
    def test_init_set(self):
        test_lon = 12.34

        # Init the class
        postcode = Store(postcode="SN25 2EG", name="Shop", lon=test_lon)

        # Check assertion
        self.assertEqual(postcode.lon, test_lon)

    def test_setter_update(self):
        test_lon = 12.34

        # Init the class
        postcode = Store(postcode="SN25 2EG", name="Shop", lon=test_lon)
        postcode.lon = test_lon

        # Check assertion
        self.assertEqual(postcode.lon, test_lon)

    def test_lat_type_init(self):
        # Exception constructor TypeError
        with self.assertRaises(TypeError):
            Store(postcode="SN25 2EG", name="Shop", lon="12.34")

    def test_lat_type_number(self):
        try:
            Store(postcode="SN25 2EG", name="Shop", lon=12)
        except IndexError:
            self.fail("Exception raised")

    def test_lat_type_setter(self):
        # Init setter TypeError
        postcode = Store(postcode="SN25 2EG", name="Shop")

        # Expect type error
        with self.assertRaises(TypeError):
            postcode.lon = "12.34"

    def test_lat_max(self):
        # Expect ValueError about out of range
        with self.assertRaises(ValueError):
            Store(postcode="SN25 2EG", name="Shop", lon=190)

    def test_lat_min(self):
        # Expect ValueError about out of range
        with self.assertRaises(ValueError):
            Store(postcode="SN25 2EG", name="Shop", lon=-190)


class TestLatitude(unittest.TestCase):
    def test_init_set(self):
        test_lat = 12.34

        # Init the class
        postcode = Store(postcode="SN25 2EG", name="Shop", lat=test_lat)

        # Check assertion
        self.assertEqual(postcode.lat, test_lat)

    def test_setter_update(self):
        test_lat = 12.34

        # Init the class
        postcode = Store(postcode="SN25 2EG", name="Shop", lat=test_lat)
        postcode.lat = test_lat

        # Check assertion
        self.assertEqual(postcode.lat, test_lat)

    def test_lat_type_init(self):
        # Exception constructor TypeError
        with self.assertRaises(TypeError):
            Store(postcode="SN25 2EG", name="Shop", lat="12.34")

    def test_lat_type_number(self):
        try:
            Store(postcode="SN25 2EG", name="Shop", lat=12)
        except IndexError:
            self.fail("Exception raised")

    def test_lat_type_setter(self):
        # Init setter TypeError
        postcode = Store(postcode="SN25 2EG", name="Shop")

        # Expect type error
        with self.assertRaises(TypeError):
            postcode.lat = "12.34"

    def test_lat_max(self):
        # Expect ValueError about out of range
        with self.assertRaises(ValueError):
            Store(postcode="SN25 2EG", name="Shop", lat=100)

    def test_lat_min(self):
        # Expect ValueError about out of range
        with self.assertRaises(ValueError):
            Store(postcode="SN25 2EG", name="Shop", lat=-100)


if __name__ == '__main__':
    unittest.main()
