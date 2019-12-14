import json
from operator import itemgetter

# Read file
with open("stores.json") as json_file:
    # Load the file resource with json
    stores = json.load(json_file)

# Sort the results
stores.sort(key=itemgetter("name"))

# Save to new file
# json.dumps(stores, indent=4, separators=(",", ":")) # pretty print

f = open("stores-sorted.json", "w")
f.write(json.dumps(stores, separators=(",", ":")))
f.close()
