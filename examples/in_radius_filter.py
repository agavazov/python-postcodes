from src.spatial import in_radius

points = [
    # In 2 km
    [23.285487, 42.653729, "IN1"],
    [23.283169, 42.654171, "IN2"],
    [23.281624, 42.658211, "IN3"],
    # Out or range
    [23.339732, 42.631884, "OUT1"],
    [23.238022, 42.663134, "OUT2"],
]

radius = 2  # in KM
radius_lon = 23.283341
radius_lat = 42.654045

result = filter(lambda x: in_radius(radius, radius_lon, radius_lat, x[0], x[1]), points)
print(list(result))
# [[23.285487, 42.653729, 'IN1'], [23.283169, 42.654171, 'IN2'], [23.281624, 42.658211, 'IN3']]
