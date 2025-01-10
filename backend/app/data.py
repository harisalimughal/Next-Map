from geojson import Feature, FeatureCollection, Point

def get_geojson_data():
    """
    Returns GeoJSON data for pins and tiles.
    """
    features = [
        Feature(
            geometry=Point((12.4924, 41.8902)),  # Rome
            properties={"region": "low", "density": 10, "name": "Rome"},
        ),
        Feature(
            geometry=Point((-0.1278, 51.5074)),  # London
            properties={"region": "high", "density": 50, "name": "London"},
        ),
        Feature(
            geometry=Point((2.3522, 48.8566)),  # Paris
            properties={"region": "medium", "density": 30, "name": "Paris"},
        ),
    ]
    return FeatureCollection(features)

def get_density_data():
    """
    Returns heatmap density data for locations.
    """
    return {
        "locations": [
            {"lat": 41.8902, "lon": 12.4924, "value": 100},  # Rome
            {"lat": 51.5074, "lon": -0.1278, "value": 200},  # London
            {"lat": 48.8566, "lon": 2.3522, "value": 150},   # Paris
        ]
    }
