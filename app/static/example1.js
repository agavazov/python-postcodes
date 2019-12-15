let example1 = {};

example1.init = () => {
    example1.ready = false;

    // Init the map
    example1.map = new mapboxgl.Map({
        container: "example1Map",
        style: "mapbox://styles/agavazov/ck45jamm420151cp7txrpvsmf",
        center: [-0.127374, 51.507585],
        zoom: 12
    });

    // Add layer
    example1.map.on("load", function () {
        example1.ready = true;

        example1.map.loadImage("./pin.png", function (error, image) {
                example1.map.addImage("pin", image);
            }
        );
    });
};

example1.run = () => {
    // Check is ready
    if (!example1.ready) {
        alert('Map is not ready. Pleas wait!');
    }

    // Prepare postcodes list
    let postcodes = $('#example1Postcodes').val().replace(/ /gi, '').split(';');

    // Get the results
    $.ajax({
        url: '/get-postcodes-coordinates',
        type: 'post',
        data: {
            postcodes: postcodes
        },
        dataType: 'json',
        success: example1.showResults
    });
};

example1.showResults = (response) => {
    // Clear the map
    if (example1.map.getLayer("markersLayer")) {
        example1.map.removeLayer("markersLayer");
    }
    if (example1.map.getSource("markersSource")) {
        example1.map.removeSource("markersSource");
    }

    // Check the response
    if (!response || !response.status || response.status !== 200 || !response.result) {
        return;
    }

    // Prepare geojson
    let boundsCoordinates = [];

    let geoJson = {
        "type": "FeatureCollection",
        "features": []
    };

    $.each(response.result, (id, row) => {
        if (!row.result || !row.result.postcode) {
            return;
        }

        boundsCoordinates.push([row.result.longitude, row.result.latitude]);

        geoJson.features.push({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    row.result.longitude,
                    row.result.latitude
                ]
            },
            "properties": {
                "title": `${row.result.postcode}`,
                "icon": "marker"
            }
        });
    });

    // Fit to bounds
    let bounds = boundsCoordinates.reduce(function (bounds, coord) {
        return bounds.extend(coord);
    }, new mapboxgl.LngLatBounds(boundsCoordinates[0], boundsCoordinates[0]));

    example1.map.fitBounds(bounds, {
        padding: 20
    });


    // Add map source
    example1.map.addSource("markersSource", {
        "type": "geojson",
        "data": geoJson
    });

    // Add layers
    example1.map.addLayer({
        "id": "markersLayer",
        "type": "symbol",
        "source": "markersSource",
        "layout": {
            "icon-image": "pin",
            "icon-size": 1,
            "icon-allow-overlap": true,
            "icon-ignore-placement": true,

            "text-allow-overlap": true,
            "text-field": ["get", "title"],
            "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
            "text-offset": [1, -0.2],
            "text-anchor": "top-left"
        }
    });
};

$(() => {
    example1.init();
});
