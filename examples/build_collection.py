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
