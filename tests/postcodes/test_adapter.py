import unittest
from src.stores import *


class TestBulkDownloaderValidRecord(unittest.TestCase):
    test_postcode: str = "LL70 9PQ"
    request_data: dict

    @classmethod
    def setUpClass(cls):
        # Make request with one existing postcode
        cls.request_data = bulk_coordinates_download([cls.test_postcode])

    def test_request_status(self):
        # Expected response status: 200
        self.assertEqual(self.request_data["status"], 200)

    def test_results_length(self):
        # Expected results length: 1
        self.assertEqual(len(self.request_data["result"]), 1)

    def test_query_match(self):
        # Expected query value
        self.assertEqual(self.request_data["result"][0]["query"], self.test_postcode)

    def test_longitude(self):
        # Expected longitude < 0
        self.assertLess(self.request_data["result"][0]["result"]["longitude"], 0)

    def test_latitude(self):
        # Expected latitude > 0
        self.assertGreater(self.request_data["result"][0]["result"]["latitude"], 0)


class TestBulkDownloaderInvalidRecord(unittest.TestCase):
    def test_no_results(self):
        test_postcode = "XXXX XXX"
        request_data = bulk_coordinates_download([test_postcode])
        self.assertEqual(request_data["result"][0]["result"], None)


class TestLoader(unittest.TestCase):
    def test_no_result_exception(self):
        collection = StoresCollection({
            "postcode": "XXXX XXX",
            "name": "Not found"
        })

        # Exception constructor ApiNoPostCodeResult
        with self.assertRaises(ApiNoPostCodeResult):
            lon_lat_loader(collection=collection, raise_error_on_missing_postcode=True)

    def test_store_file(self):
        collection = StoresCollection()
        collection.import_json_file("./tests/stores.json")

        lon_lat_loader(collection)

        # Expected latitude > 0
        self.assertGreater(collection.stores[0].lat, 0)


if __name__ == "__main__":
    unittest.main()
