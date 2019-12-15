import json
from json.decoder import JSONDecodeError
from urllib import request
from urllib.parse import urlencode
from . import StoresCollection
from .errors import *


def lon_lat_loader(collection: StoresCollection, raise_error_on_missing_postcode: bool = False):
    """
    Set lot & lat for each store

    This method will get all postcodes from the stores collection
    And will split them into chunks for bul request/s
    In order to optimize time and resources

    Args:
        collection (StoresCollection): Stores collection
        raise_error_on_missing_postcode (bool, optional): If there is no data for some store it will raise error

    """

    # Maximum chunk size in for bulk request in postcodes.io
    max_request_chunk_size = 100

    # Collect all unique postcodes
    all_postcodes = []

    for store in collection.stores:
        # Check for duplicates
        if store.postcode in all_postcodes:
            continue

        # Append the postcode
        all_postcodes.append(store.postcode)

    # Loop the chunks ang get bulk data
    for chunk in list(chunks(all_postcodes, max_request_chunk_size)):
        postcodes_data = bulk_coordinates_download(chunk)

        # Check response object
        if not isinstance(postcodes_data, dict):
            continue

        # Check the response code
        if postcodes_data['status'] is not 200:
            continue

        # Check is there any
        if not isinstance(postcodes_data['result'], list):
            continue

        # Map the results
        for row in postcodes_data['result']:
            # Check is any data for the specific postcode
            if row['result'] is None:
                if raise_error_on_missing_postcode:
                    raise ApiNoPostCodeResult("No data for " + row['query'])
                else:
                    continue

            # Get the needed data
            postcode = row['result']['postcode']
            lon = row['result']['longitude']
            lat = row['result']['latitude']

            # Loop the stores and set the coordinates
            for index, store in enumerate(collection.stores):
                # Check for match
                if store.postcode == postcode:
                    collection.stores[index].lon = lon
                    collection.stores[index].lat = lat


def bulk_coordinates_download(postcodes: [str]) -> [object]:
    """
    Make bulk request with all postcodes

    Args:
        postcodes ([str]): List of the postcodes

    """

    api_url = "https://api.postcodes.io/postcodes"

    params = {'postcodes[]': postcodes}

    # Build url encoded data
    data = urlencode(params, True)

    # Convert string to byte
    data = data.encode('utf-8')

    # Prepare the request
    req = request.Request(api_url, data=data)

    # Get the response
    try:
        resp = request.urlopen(req)
    except URLError:
        raise ApiConnectionError("Connection problem with " + api_url)

    # Parse from JSON
    try:
        return json.loads(resp.read())
    except JSONDecodeError:
        return []


def chunks(elements, chunk_size) -> []:
    """
    N-sized chunks from lst
    (https://stackoverflow.com/a/1751478)
    """
    chunk_size = max(1, chunk_size)
    return (elements[i:i + chunk_size] for i in range(0, len(elements), chunk_size))
