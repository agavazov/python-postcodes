import json
from math import sin, cos, sqrt, atan2, radians

# Read file
with open("stores-geo.json") as json_file:
    # Load the file resource with json
    stores = json.load(json_file)


def points_distance(lat1, lng1, lat2, lng2):
    R = 6373.0

    lat1 = radians(lat1)
    lng1 = radians(lng1)

    lat2 = radians(lat2)
    lng2 = radians(lng2)

    dlon = lng2 - lng1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


radius_lat = 52.002562
radius_lng = 0.724652
radius_distance = 100

for row in stores:
    point_distance = points_distance(radius_lat, radius_lng, row["lat"], row["lng"])
    if radius_distance >= point_distance:
        print("distance for : " + row["postcode"] + "is " + str(point_distance))
