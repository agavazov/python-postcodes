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
