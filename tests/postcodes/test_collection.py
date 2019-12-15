import unittest
from json.decoder import JSONDecodeError
from src.stores import Store, StoresCollection
from src.stores.errors import *


class TestAppend(unittest.TestCase):
    def test_append_stores(self):
        # Append stores
        store2 = Store(postcode="SN22 222", name="Store 2", lon=2, lat=2)
        store3 = Store(postcode="SN33 333", name="Store 3", lon=3, lat=3)

        # Append from constructor as array with mixed types
        collection = StoresCollection(stores=[{
            "postcode": "SN25 2EG",
            "name": "Store 1",
            "lon": 1,
            "lat": 1
        }, store2])

        # Append single record
        collection.append(store3)

        # Check assertion
        self.assertEqual(collection.stores[0].name, "Store 1")
        self.assertEqual(collection.stores[1].name, "Store 2")
        self.assertEqual(collection.stores[2].name, "Store 3")

        # Instance compare
        self.assertEqual(collection.stores[1], store2)

    def test_append_wrong_data(self):
        # Append stores
        collection = StoresCollection()

        # Exception constructor StoreInvalidDefinitionError
        with self.assertRaises(StoreInvalidDefinitionError):
            collection.append({
                "foo": "bar"
            })


class TestSort(unittest.TestCase):
    collection: StoresCollection

    @classmethod
    def setUpClass(cls):
        # Set global collection for sort tests
        cls.collection = StoresCollection([
            Store(postcode="ZXDT 333", name="AB", lon=2, lat=2),
            Store(postcode="ASFR 333", name="aA", lon=1, lat=1),
            Store(postcode="UYEE 222", name="AC", lon=3, lat=3),
        ])

    def test_name_sort(self):
        # Sort
        self.collection.sort(sort_key="name")

        # Check assertion
        self.assertEqual(self.collection.stores[0].name, "aA")
        self.assertEqual(self.collection.stores[1].name, "AB")
        self.assertEqual(self.collection.stores[2].name, "AC")

    def test_name_sort_reverse(self):
        # Reverse sort
        self.collection.sort(sort_key="name", reverse=True)

        # Check assertion
        self.assertEqual(self.collection.stores[0].name, "AC")
        self.assertEqual(self.collection.stores[1].name, "AB")
        self.assertEqual(self.collection.stores[2].name, "aA")

    def test_append_wrong_sort_ket(self):
        # Exception constructor WrongSortKeyError
        with self.assertRaises(WrongSortKeyError):
            self.collection.sort(sort_key="WRONG")


class TestImport(unittest.TestCase):
    def test_file_import(self):
        collection = StoresCollection()
        collection.import_json_file("./tests/stores.json")

        self.assertGreater(len(collection.stores), 0)

    def test_non_exist_file(self):
        collection = StoresCollection()

        # Exception constructor InvalidJsonFile
        with self.assertRaises(InvalidJsonFile):
            collection.import_json_file("./random/a/s/d/f.json")

    def test_non_json_file(self):
        collection = StoresCollection()

        # Exception constructor InvalidJsonFile
        with self.assertRaises(InvalidJsonFile):
            collection.import_json_file(__file__)


class TestJsonImport(unittest.TestCase):
    def test_json_import(self):
        collection = StoresCollection()
        collection.import_json('[{"name": "Shop", "postcode": "ASD FDS"}]')

        self.assertEqual(len(collection.stores), 1)

    def test_json_import_overwrite(self):
        collection = StoresCollection()

        # Append one record
        collection.import_json('[{"name": "Shop", "postcode": "ASD FDS"}]')
        self.assertEqual(len(collection.stores), 1)

        # Append second record
        collection.import_json('[{"name": "Shop 2", "postcode": "ASD FDS"}]')
        self.assertEqual(len(collection.stores), 2)

        # Append one record + Overwrite
        collection.import_json('[{"name": "Shop 2", "postcode": "ASD FDS"}]', True)
        self.assertEqual(len(collection.stores), 1)

    def test_incorrect_json_string(self):
        collection = StoresCollection()

        # Exception constructor JSONDecodeError
        with self.assertRaises(JSONDecodeError):
            collection.import_json('ASDF')

    def test_wrong_json_format(self):
        collection = StoresCollection()

        # Exception constructor StoreInvalidDefinitionError
        with self.assertRaises(StoreInvalidDefinitionError):
            collection.import_json('[{"A": "B", "C": "D"}]')

    def test_export_json(self):
        collection = StoresCollection([
            {"name": "Shop", "postcode": "ASD FDS"}
        ])

        output_json = collection.export_json()
        self.assertGreater(len(output_json), 0)


if __name__ == "__main__":
    unittest.main()
