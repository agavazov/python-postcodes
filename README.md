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

Simple way to get postcodes longitude, latitude and more information:
```python
from src.stores import adapter

postcodes_data = adapter.bulk_coordinates_download([
    "B60 3GP",
    "G69 6NA",
    "G40 2AS",
    "RH6 9SE",
    "TN36 4EG",
    "PR3 0NN",
])

print(postcodes_data)
```

Build collection:
```python
from src.stores import *

# Init collection
collection = StoresCollection([
    {
        "postcode": "NN14 1TE",
        "name": "Store 01"
    },
    {
        "postcode": "KY13 9HJ",
        "name": "Store 02"
    },
    Store("CM19 4LU", "Store 3"),
    Store(postcode="ST7 8NY", name="Store 04")
])

# Append array
collection.append([
    {
        "postcode": "PA64 6AP",
        "name": "Store 06"
    },
    {
        "postcode": "KY13 9HJ",
        "name": "Store 07"
    }
])

# Append single record
collection.append({
    "postcode": "GU19 5ND",
    "name": "Store 08",
    "lon": -0.686846,
    "lat": 51.361558
})

# Append Store object
collection.append(Store("CA28 7DG", "Store 09", -3.588092, 54.547847))

# Append JSON
collection.import_json('{"postcode": "AB12 3HH", "name": "Store 10", "lon": -2.082634, "lat": 57.10418}')

# Add JSON file
collection.import_json_file("./../tests/stores.json")

# Get longitude and latitude for each store
geo_collection_loader(collection)

# Sort the collection
collection.sort("postcode")  # by postcode
collection.sort("lon")  # by longitude
collection.sort("lat")  # by latitude
collection.sort("name")  # by name

# Export to JSON file
collection.export_json_file("./build_collection.json")

# Dump raw JSON string
print(collection.export_json())
```

## Flask web examples
### Example: src.stores.adapter.bulk_coordinates_download
Bulk postcode finder (per 100 chunks)

![png](https://raw.githubusercontent.com/agavazov/python-postcodes/master/examples/images/flask-example-1.jpg)
