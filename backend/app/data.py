from geojson import Feature, FeatureCollection, Point

def get_geojson_data():
    """
    Returns GeoJSON data for pins and tiles.
    """
    features = [
        Feature(
            geometry=Point((12.4924, 41.8902)),  # Rome
            properties={"region": "low", "density": 1100, "name": "Rome"},
        ),
        Feature(
            geometry=Point((-0.1278, 51.5074)),  # London
            properties={"region": "high", "density": 1200, "name": "London"},
        ),
        Feature(
            geometry=Point((2.3522, 48.8566)),  # Paris
            properties={"region": "medium", "density": 15400, "name": "Paris"},
        ),
        Feature( geometry=Point((77.2090, 28.6139)), # New Delhi 
                properties={"region": "high", "density": 1300, "name": "New Delhi"}, 
                ), 
        Feature( geometry=Point((139.6917, 35.6895)), # Tokyo 
                properties={"region": "very high", "density": 1400, "name": "Tokyo"}, 
                ), 
        Feature( geometry=Point((126.9780, 37.5665)), # Seoul 
                properties={"region": "medium", "density": 12500, "name": "Seoul"}, 
                ), 
        Feature( geometry=Point((103.8198, 1.3521)), # Singapore 
                properties={"region": "high", "density": 1280, "name": "Singapore"}, 
                ), 
        Feature( geometry=Point((106.8650, -6.2088)), # Jakarta 
                properties={"region": "medium", "density": 1220, "name": "Jakarta"}, 
                ),
        Feature( geometry=Point((73.0479, 33.6844)), # Pakistan
                properties={"region": "medium", "density": 1600, "name": "Pakistan"}, 
                ),
    ]
    return FeatureCollection(features)

def get_density_data():
    """
    Returns heatmap density data for locations.
    """
    return {
        "locations": [
           {"lat": 41.8902, "lon": 12.4924, "density": 1100,"name":"Rome"},  # Rome
           {"lat": 51.5074, "lon": -0.1278, "density": 1200,"name":"London"}, # London 
           {"lat": 48.8566, "lon": 2.3522, "density": 15400,"name":"Paris"}, # Paris 
           {"lat": 28.6139, "lon": 77.2090, "density": 1300,"name":"New Delhi"}, # New Delhi 
           {"lat": 35.6895, "lon": 139.6917, "density": 1400,"name":"Tokyo"}, # Tokyo 
           {"lat": 37.5665, "lon": 126.9780, "density": 12500,"name":"Seoul"}, # Seoul 
           {"lat": 1.3521, "lon": 103.8198, "density": 1280,"name":"Singapore"}, # Singapore 
           {"lat": -6.2088, "lon": 106.8650, "density": 1220,"name":"Jakarta"}, # Jakarta
           {"lat": 33.6844, "lon": 73.0479, "density": 1600, "name":"Pakistan"} # Pakistan
        ]
    }
