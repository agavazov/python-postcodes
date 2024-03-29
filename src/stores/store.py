from .errors import *


class Store:
    """
    Store record

    Each postcode record contains basic information like name
    and coordinates in WGS84 geographic system

    """

    def __init__(self, postcode: str, name: str, lon: float = None, lat: float = None):
        """
        Create new store record.

        Args:
            postcode (str): Postcode identification (it can be international)
            name (str): Simple information about the postcode (like place name)
            lon (float, optional): Longitude of the postcode in WGS84
            lat (float, optional): Latitude of the postcode in WGS84

        """

        # Set constructor values
        self.postcode = postcode
        self.name = name
        self.lon = lon
        self.lat = lat

    @property
    def postcode(self) -> str:
        """
        "postcode" getter
        """

        return self._postcode

    @postcode.setter
    def postcode(self, postcode: str):
        """
        "postcode" setter

        The postcode can be international so the minimal requirement is to be
        at least 1 character length. If you want to use
        UK postcode only: https://pypi.org/project/uk-postcode-utils/

        Args:
            postcode (str): Postcode identification

        """

        # Validation the type of the postcode
        if not isinstance(postcode, str):
            raise StoreInvalidDefinitionError("code value must be a string type")

        # Validation of the length
        if len(postcode) < 1:
            raise StoreInvalidDefinitionError("code must be at leas 1 character")

        self._postcode = postcode

    @property
    def name(self) -> str:
        """
        "name" getter
        """

        return self._name

    @name.setter
    def name(self, name: str):
        """
        "name" setter

        The postcode can be international so the minimal requirement is to be
        at least 1 character length

        Args:
            name (str): Simple information about the postcode (like place name)

        """

        # Validation the type of the name
        if not isinstance(name, str):
            raise StoreInvalidDefinitionError("name value must be a string type")

        # Validation of the length
        if len(name) < 1:
            raise StoreInvalidDefinitionError("name must be at leas 1 character")

        self._name = name

    @property
    def lon(self) -> float:
        """
        "lon" getter
        """

        return self._lon

    @lon.setter
    def lon(self, lon: float):
        """
        "lon" setter

        Set Longitude in the range -180 and +180 specifying coordinates
        west and east of the Prime Meridian

        Args:
            lon (float, optional): Longitude of the postcode in WGS84

        """

        # lon param can be null
        if lon is None:
            self._lon = lon
            return

        # Validation the type of the lon
        if not isinstance(lon, float) and not isinstance(lon, int):
            raise StoreInvalidDefinitionError("lon value must be a float type")

        # Check for range between -180 and 180
        if lon < -180 or lon > 180:
            raise StoreInvalidDefinitionError("lon value must be a float type")

        self._lon = lon

    @property
    def lat(self) -> float:
        """
        "lat" getter
        """

        return self._lat

    @lat.setter
    def lat(self, lat: float):
        """
        "lat" setter

        Set Latitude in the range -90 and +90 for the
        southern and northern hemisphere respectively

        Args:
            lat (float, optional): Latitude of the postcode in WGS84

        """

        # lat param can be null
        if lat is None:
            self._lat = lat
            return

        # Validation the type of the lat
        if not isinstance(lat, float) and not isinstance(lat, int):
            raise StoreInvalidDefinitionError("lat value must be a float type")

        # Check for range between -90 and 90
        if lat < -90 or lat > 90:
            raise StoreInvalidDefinitionError("lat value must be a float type")

        self._lat = lat

    def serialize(self) -> object:
        """
        export current object

        With serialization you can have clean object
        which can be used for JSON.dump or other actions
        The main propose is to be unwrapped from Store class

        """

        return {
            "postcode": self.postcode,
            "name": self.name,
            "lon": self.lon,
            "lat": self.lat
        }
