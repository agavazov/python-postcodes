from . import Store
import json


class PostcodesCollection:
    """@todo
    """

    postcodes: [Store] = []

    def __init__(self, postcodes=None, postcodes_file: str = None):
        """@todo
        """

        # Append postcodes
        if postcodes is not None:
            self.append(postcodes)

        # Import file
        if postcodes_file is not None:
            self.import_file(postcodes_file, False)

    def append(self, postcodes):
        """@todo
        str or Postcode or array
        @todo
        """

        # If the input is not array the make it
        if not isinstance(postcodes, list):
            postcodes = [postcodes]

        # Validate each item
        for index, postcode in enumerate(postcodes):
            # If the postcode is not instance of Postcode class the make it
            if isinstance(postcode, dict):
                # Apply dictionary keys as arguments
                print(postcode)
                postcodes[index] = Store(**postcode)
            elif not isinstance(postcode, Store):
                # Validate the final type
                raise ValueError("postcode item must be a Dictionary or a Postcode instance")

        # Merge lists
        self.postcodes += postcodes

    def sort(self, by_key: str, reverse: bool = False):
        """@todo
        @todo
        """

    def import_file(self, file_path: str, overwrite: bool = False):
        """@todo
        @todo
        """

        with open(file_path) as json_data:  # type: str
            self.import_json(json_data, overwrite)

    def import_json(self, json_data: str, overwrite: bool = False):
        """@todo
        @todo
        """

        if overwrite:
            self.postcodes = []

        self.append(json.load(json_data))

    def export_file(self, file_path: str):
        """@todo
        @todo
        """
