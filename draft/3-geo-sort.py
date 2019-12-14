import json
from operator import itemgetter

# Read file
with open("stores-geo.json") as json_file:
    # Load the file resource with json
    stores = json.load(json_file)

# Sort the results
stores.sort(key=itemgetter("lat"), reverse=True)

# Save
f = open("stores-geo-sorted.json", "w")
f.write(json.dumps(stores, separators=(",", ":")))
f.close()
