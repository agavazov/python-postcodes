let example2 = {};

example2.init = () => {
    example2.ready = false;

    // Init the map
    example2.map = new mapboxgl.Map({
        container: "example2Map",
        style: "mapbox://styles/agavazov/ck45jamm420151cp7txrpvsmf",
        center: [-0.127374, 51.507585],
        zoom: 12
    });

    // Add layer
    example2.map.on("load", function () {
        example2.ready = true;

        example2.map.loadImage("./pin.png", function (error, image) {
                example2.map.addImage("pin", image);
            }
        );
    });
};

example2.run = () => {
    // Check is ready
    if (!example2.ready) {
        alert('Map is not ready. Pleas wait!');
    }

    // Prepare postcodes list
    let postcodes = $('#example2Postcodes').val().replace(/ /gi, '').split(';');
    let radius = parseInt($('#example2RadiusRange').val());
    let radiusPostcode = $('#example2RadiusPostcode').val();

    if (!radiusPostcode) {
        $('#example2RadiusPostcode').focus();
        alert('Please enter radius postcode');
        return;
    }

    // Get the results
    $.ajax({
        url: '/get-postcodes-radius',
        type: 'post',
        data: {
            postcodes: postcodes,
            radius: radius,
            radiusPostcode: radiusPostcode,
        },
        dataType: 'json',
        success: example2.showResults
    });
};

example2.showResults = (response) => {
    alert('Under construction');
    // @todo
    return;

    // Clear the map
    if (example2.map.getLayer("markersLayer")) {
        example2.map.removeLayer("markersLayer");
    }
    if (example2.map.getSource("markersSource")) {
        example2.map.removeSource("markersSource");
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

    example2.map.fitBounds(bounds, {
        padding: 20
    });


    // Add map source
    example2.map.addSource("markersSource", {
        "type": "geojson",
        "data": geoJson
    });

    // Add layers
    example2.map.addLayer({
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
    example2.init();
});
