from math import sin, cos, sqrt, atan2, radians


def points_distance(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate two points distance in KM

    The original source of the function is from here https://stackoverflow.com/a/19412565
    Which is classical GIS solution. The only change I`ve made is "longitude 1st"
    Because "longitude 1st" is the classical way how the spatial databases works
    or GeoJSON sets the coordinates

    Args:
        lon1 (float): Longitude of the first point
        lat1 (float): Latitude of the first point
        lon2 (float): Longitude of the second point
        lat2 (float): Latitude of the second point

    """

    earth_radius = 6372.795

    lon1 = radians(lon1)
    lat1 = radians(lat1)

    lon2 = radians(lon2)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius * c

    return distance


def in_radius(radius: float, center_lon: float, center_lat: float, point_lon: float, point_lat: float) -> float:
    """
    Filter function for radius check

    Example:
        points = [
            # In 2 km
            [23.285487, 42.653729, "IN1"],
            [23.283169, 42.654171, "IN2"],
            [23.281624, 42.658211, "IN3"],
            # Out or range
            [23.339732, 42.631884, "OUT1"],
            [23.238022, 42.663134, "OUT2"],
        ]
        result = filter(lambda x: in_radius(2, 23.283341, 42.654045, x[0], x[1]), points)
        print(list(result))

    Args:
        radius (float): Radius in KM
        center_lon (float): Radius center longitude
        center_lat (float): Radius center latitude
        point_lon (float): Point longitude
        point_lat (float): Point latitude

    """

    # Check for null coordinates
    if point_lon is None or point_lat is None:
        return False

    # Distance check
    return points_distance(center_lon, center_lat, point_lon, point_lat) <= radius
