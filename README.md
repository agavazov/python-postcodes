# My first python code
[![Build Status](https://travis-ci.org/agavazov/python-postcodes.svg?branch=master)](https://travis-ci.org/agavazov/python-postcodes)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Test the project
The unittests are based on `unittest` package and they are located in `./tests` directory.

To start them you have to run `python setup.py test`

## Examples
Get stores from file, fill lon/lat and make radius search (via filter):
```python
from src.stores import *
from src.spatial import *

# Init collection
collection = StoresCollection(stores_file="./../tests/stores.json")

# Alphabetical order
collection.sort("name")

# Get longitude and latitude for each store
geo_collection_loader(collection)

# Set the radius
radius_range = 20  # in KM
radius = postcode_coordinates("BN3 7PN")

# Filter the results
collection.filter(lambda x: in_radius(radius_range, radius["lon"], radius["lat"], x.lon, x.lat))

# Sort from north to south
collection.sort("lat")

# Export to JSON
print(collection.export_json())
```

Simple radius search:
```python
from src.spatial import in_radius

points = [
    # In 2 km
    [23.285487, 42.653729, "IN1"],
    [23.283169, 42.654171, "IN2"],
    [23.281624, 42.658211, "IN3"],
    # Out or range
    [23.339732, 42.631884, "OUT1"],
    [23.238022, 42.663134, "OUT2"],
]

radius = 2  # in KM
radius_lon = 23.283341
radius_lat = 42.654045

result = filter(lambda x: in_radius(radius, radius_lon, radius_lat, x[0], x[1]), points)
print(list(result))
# [[23.285487, 42.653729, 'IN1'], [23.283169, 42.654171, 'IN2'], [23.281624, 42.658211, 'IN3']]
```