from . import Postcode


class PostcodesCollection:
    """@todo
    """

    postcodes: [Postcode] = []

    def __init__(self, postcodes: [Postcode] = None, postcodes_file: str = None):
        """@todo
        @todo
        """

        if postcodes is not None:
            self.append(postcodes)

        if postcodes_file is not None:
            self.import_file(postcodes_file)

    def append(self, postcode):
        """@todo
        str or Postcode or array
        @todo
        """

        self.postcodes.append(postcode)

    def sort(self, by_key: str, reverse: bool = False):
        """@todo
        @todo
        """

    def import_file(self, file_path: str, overwrite: bool = False):
        """@todo
        @todo
        """

    def export_file(self, file_path: str):
        """@todo
        @todo
        """
