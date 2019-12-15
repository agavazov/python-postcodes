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
