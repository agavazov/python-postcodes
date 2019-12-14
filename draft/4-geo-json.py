import json
from operator import itemgetter

# Read file
with open("stores-geo-sorted.json") as json_file:
    # Load the file resource with json
    stores = json.load(json_file)

# Build geo json
geoJson = {
    "type": "FeatureCollection",
    "features": []
}

position = 0
for row in stores:
    position += 1

    geoJson["features"].append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                row["lng"],
                row["lat"]
            ]
        },
        "properties": {
            "name": row["name"],
            "postcode": row["postcode"],
            "position": position
        }
    })

# Save to new file
f = open("stores-geo-sorted.geojson", "w")
f.write(json.dumps(geoJson, separators=(",", ":")))
f.close()
