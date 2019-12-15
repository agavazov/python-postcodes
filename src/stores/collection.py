from . import Store
from .errors import *
import json
from json.decoder import JSONDecodeError


class StoresCollection:
    """
    Collection of the stores

    The purpose of this class is to collect all registered
    stores so that it can add additional functionality when
    working with them

    """

    # Registered stores (aways as a Store class)
    stores: [Store] = []

    def __init__(self, stores=None, stores_file: str = None):
        """
        Create new store record.

        Example:
            StoresCollection({
                "postcode": "Axb",
                "name": "Gamxa"
            })

            StoresCollection([{"postcode": "Axb", "name": "Gamxa"}, {"postcode": "Asd", "name": "Gfds"}])
            StoresCollection(Postcode(...))
            StoresCollection([Postcode(...)])

        Args:
            stores (list, object, Store, [Store], [object], optional): Append the stores records.
            stores_file (str, optional): Import directly JSON file with Stores data

        """

        # Set empty collection list
        self.stores = []

        # Append stores
        if stores is not None:
            self.append(stores)

        # Import file
        if stores_file is not None:
            self.import_json_file(stores_file, False)

    def append(self, stores):
        """
        Create new store record.

        Example:
            collection.append({
                "postcode": "Axb",
                "name": "Gamxa"
            })

            collection.append([{"postcode": "Axb", "name": "Gamxa"}, {"postcode": "Asd", "name": "Gfds"}])
            collection.append(Postcode(...))
            collection.append([Postcode(...)])

        Args:
            stores (list, object, Store, [Store], [object], optional): Append the stores records.

        """

        # If the input is not array the make it
        if not isinstance(stores, list):
            stores = [stores]

        # Validate each item
        for index, store in enumerate(stores):
            # If the store is not instance of Store class the make it
            if isinstance(store, dict):
                # Apply dictionary keys as arguments
                try:
                    stores[index] = Store(**store)
                except TypeError:
                    raise StoreInvalidDefinitionError("Dictionary keys are not as Store class expect")
            elif not isinstance(store, Store):
                # Validate the final type
                raise StoreInvalidDefinitionError("Store item must be a Dictionary or a Store instance")

        # Merge lists
        self.stores += stores

    def sort(self, sort_key: str, reverse: bool = False):
        """
        Sort stores list

        Args:
            sort_key (str): The key by which the records will be sorted
            reverse (bool, optional): Reverse sorting

        """

        # Check is the sort key existing in the Store properties
        if not hasattr(Store, sort_key):
            raise WrongSortKeyError("The sort key is not defined in Store class")

        # key is not dynamic -> self.stores.sort(key=lambda store: store.postcode, reverse=reverse)
        # there is a problem with None -> self.stores.sort(key=lambda store: getattr(store, sort_key), reverse=reverse)

        # Final solution (sort by dynamic key and works with None including case insensitive)
        self.stores.sort(key=lambda x: (getattr(x, sort_key) is None,  # Check for None
                                        getattr(x, sort_key).lower() if isinstance(getattr(x, sort_key), str)  # lower
                                        else getattr(x, sort_key)),
                         reverse=reverse)

    def filter(self, filter_rule):
        """
        Filter apply

        Args:
            filter_rule: Apply filter rule directly to current store list

        """

        self.stores = list(filter(filter_rule, self.stores))

    def import_json(self, json_data: str, overwrite: bool = False):
        """
        Sort stores list

        Args:
            json_data (str): JSON data which will be appended
            overwrite (bool, optional): Clear the old records and append the JSON list

        """

        # Remove old records
        if overwrite:
            self.stores = []

        # Append new records
        self.append(json.loads(json_data))

    def export_json(self) -> str:
        """
        Export current stores list to JSON
        """

        # New empty list where all serialized object will be collected
        json_data = []

        # Collect and serialize the Store objects
        for store in self.stores:
            json_data.append(store.serialize())

        # Export to JSON
        return json.dumps(json_data, separators=(",", ":"))

    def import_json_file(self, file_path: str, overwrite: bool = False):
        """
        Import stores list from JSON file

        Args:
            file_path (str): The path to the JSON file
            overwrite (bool, optional): Clear the old records and append the JSON list

        """

        # Read the file
        try:
            with open(file_path) as json_data:
                # Cast the file data to string and send it to self.import_json
                self.import_json(json_data.read(), overwrite)
        except FileNotFoundError:
            raise InvalidJsonFile("File not found")
        except JSONDecodeError:
            raise InvalidJsonFile("File content is not JSON")

    def export_json_file(self, file_path: str):
        """
        Export current stores list to JSON file

        Args:
            file_path (str): The path to the JSON file

        """

        # Open the file and writes the data
        f = open(file_path, "w")
        f.write(self.export_json())
        f.close()
