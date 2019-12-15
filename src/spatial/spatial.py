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
        points = [{lon: 1, lat: 2}, {lon: 1, lat: 2}]
        @todo write the example

    Args:
        radius (float): Radius in KM
        center_lon (float): Radius center longitude
        center_lat (float): Radius center latitude
        point_lon (float): Point longitude
        point_lat (float): Point latitude

    """

    return points_distance(center_lon, center_lat, point_lon, point_lat) <= radius
