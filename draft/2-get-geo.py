import json
import urllib.request
import urllib.parse

# Read file
with open("stores-sorted.json") as json_file:
    # Load the file resource with json
    stores = json.load(json_file)

# Test my 1st request
# hello_there = urllib.request.urlopen("http://api.postcodes.io/postcodes/SW17%200BW").read()
# print(json.loads(hello_there))
# print(json.loads(hello_there)["result"]["longitude"])
# exit()

# Test with bad request
# try:
#     hello_there = urllib.request.urlopen("http://api.postcodes.io/postcodes/").read()
# except urllib.error.HTTPError as e:
#     hello_there = e.read()
# print(json.loads(hello_there))
# exit()

# Loop
newStores = []
for row in stores:
    print("get data for: " + row["postcode"])

    # Make single request
    try:
        postcode = urllib.parse.quote(row["postcode"])
        postcode_data = urllib.request.urlopen("http://api.postcodes.io/postcodes/" + postcode).read()
        postcode_data = json.loads(postcode_data)
        row["lat"] = postcode_data["result"]["latitude"]
        row["lng"] = postcode_data["result"]["longitude"]

        newStores.append(row)
    except urllib.error.HTTPError as e:
        print("NOOOOO!")

# Save to new file
f = open("stores-geo.json", "w")
f.write(json.dumps(newStores, separators=(",", ":")))
f.close()
