# data.py

from geojson import Feature, FeatureCollection, Point
from geopy.geocoders import Nominatim

# Simulated call data
call_data = [
    "+923001234567", "+923001234568", "+442071838750", "+81312345678",
    "+923001234569", "+923001234570", "+923001234571", "+923001234572"
]

def get_geojson_data(call_data=call_data):
    """
    Returns GeoJSON data for pins and tiles based on country codes.
    """
    geolocator = Nominatim(user_agent="geojson-generator")
    country_code_to_properties = {
        "+39": {"region": "low", "density": 1100, "name": "Rome"},
        "+44": {"region": "high", "density": 1200, "name": "London"},
        "+33": {"region": "medium", "density": 15400, "name": "Paris"},
        "+91": {"region": "high", "density": 1300, "name": "New Delhi"},
        "+81": {"region": "very high", "density": 1400, "name": "Tokyo"},
        "+82": {"region": "medium", "density": 12500, "name": "Seoul"},
        "+65": {"region": "high", "density": 1280, "name": "Singapore"},
        "+62": {"region": "medium", "density": 1220, "name": "Jakarta"},
        "+92": {"region": "medium", "density": 0, "name": "Pakistan"},
    }

    # Count calls for country code +92
    call_count = sum(1 for call in call_data if call.startswith("+92"))
    print(f"Number of calls for +92: {call_count}")
    
    # Update the density for +92 based on call count
    if "+92" in country_code_to_properties:
        country_code_to_properties["+92"]["density"] += call_count

    features = []
    for country_code, properties in country_code_to_properties.items():
        try:
            location = geolocator.geocode(properties["name"])
            if location:
                feature = Feature(
                    geometry=Point((location.longitude, location.latitude)),
                    properties={
                        "country_code": country_code,
                        "region": properties["region"],
                        "density": properties["density"],
                        "name": properties["name"],
                    },
                )
                features.append(feature)
            else:
                print(f"Could not find location for {properties['name']}")
        except Exception as e:
            print(f"Error fetching location for {properties['name']}: {e}")
    return FeatureCollection(features)

def get_density_data(call_data=call_data):
    """
    Returns heatmap density data for locations based on country codes.
    """
    geojson_data = get_geojson_data(call_data)
    return {
        "locations": [
            {
                "lat": feature["geometry"]["coordinates"][1],
                "lon": feature["geometry"]["coordinates"][0],
                "density": feature["properties"]["density"],
                "name": feature["properties"]["name"],
            }
            for feature in geojson_data["features"]
        ]
    }
