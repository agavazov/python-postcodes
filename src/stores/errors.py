from urllib.error import URLError


class StoreInvalidDefinitionError(TypeError):
    """
    The store object is not well formatted
    """


class WrongSortKeyError(KeyError):
    """
    The sort key not persist in Store properties
    """


class InvalidJsonFile(Exception):
    """
    The file not contains valid JSON or the file is not found
    """


class ApiConnectionError(URLError):
    """
    Can not connect to the postcode API
    """


class ApiNoPostCodeResult(Exception):
    """
    There is no data for the specific postcode
    """
