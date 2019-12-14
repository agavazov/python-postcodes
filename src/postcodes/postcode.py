class Postcode:
    """Single postcode record.

    Each postcode record contains basic information like name
    and coordinates in WGS84 geographic system

    """

    def __init__(self, code: str, name: str, lon: float = None, lat: float = None):
        """Create new postcode record.

        Args:
            code (str): Postcode identification
            name (str): Simple information about the postcode (like place name)
            lon (float, optional): Longitude of the postcode in WGS84
            lat (float, optional): Latitude of the postcode in WGS84

        """

        # Set constructor values
        self.code = code
        self.name = name
        self.lon = lon
        self.lat = lat

    @property
    def code(self) -> str:
        """code getter"""

        return self._code

    @code.setter
    def code(self, code: str):
        """code setter

        The postcode can be international so the minimal requirement is to be
        at least 1 character length

        Args:
            code (str): Postcode identification

        """

        # Validation the type of the code
        if not isinstance(code, str):
            raise TypeError("code value must be a string type")

        # Validation of the length
        if len(code) < 0:
            raise ValueError("code must be at leas 1 character")

        self._code = code

    @property
    def name(self) -> str:
        """name getter"""

        return self._name

    @name.setter
    def name(self, name: str):
        """name setter

        The postcode can be international so the minimal requirement is to be
        at least 1 character length

        Args:
            name (str): Simple information about the postcode (like place name)

        """

        # Validation the type of the name
        if not isinstance(name, str):
            raise TypeError("name value must be a string type")

        self._name = name

    @property
    def lon(self) -> float:
        """lon getter"""

        return self._lon

    @lon.setter
    def lon(self, lon: float):
        """lon setter

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
        if not isinstance(lon, float):
            raise TypeError("lon value must be a float type")

        # Check for range between -180 and 180
        if lon < -180 or lon > 180:
            raise TypeError("lon value must be a float type")

        self._lon = lon

    @property
    def lat(self) -> float:
        """lat getter"""

        return self._lat

    @lat.setter
    def lat(self, lat: float):
        """lat setter

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
        if not isinstance(lat, float):
            raise TypeError("lat value must be a float type")

        # Check for range between -180 and 180
        if lat < -180 or lat > 180:
            raise TypeError("lat value must be a float type")

        self._lat = lat