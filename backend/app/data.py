from geojson import Feature, FeatureCollection, Point
from geopy.geocoders import Nominatim

def get_geojson_data():
    """
    Returns GeoJSON data for pins and tiles based on country codes.
    """
    geolocator = Nominatim(user_agent="geojson-generator")

    # Mapping of country codes to properties
    country_code_to_properties = {
        "+39": {"region": "low", "density": 1100, "name": "Rome"},
        "+44": {"region": "high", "density": 1200, "name": "London"},
        "+33": {"region": "medium", "density": 15400, "name": "Paris"},
        "+91": {"region": "high", "density": 1300, "name": "New Delhi"},
        "+81": {"region": "very high", "density": 1400, "name": "Tokyo"},
        "+82": {"region": "medium", "density": 12500, "name": "Seoul"},
        "+65": {"region": "high", "density": 1280, "name": "Singapore"},
        "+62": {"region": "medium", "density": 1220, "name": "Jakarta"},
        "+92": {"region": "medium", "density": 1600, "name": "Pakistan"},
    }

    features = []

    for country_code, properties in country_code_to_properties.items():
        try:
            # Fetch location details using the country name
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

def get_density_data():
    """
    Returns heatmap density data for locations based on country codes.
    """
    geolocator = Nominatim(user_agent="geojson-generator")

    country_code_to_properties = {
        "+39": {"density": 1100, "name": "Rome"},
        "+44": {"density": 1200, "name": "London"},
        "+33": {"density": 15400, "name": "Paris"},
        "+91": {"density": 1300, "name": "New Delhi"},
        "+81": {"density": 1400, "name": "Tokyo"},
        "+82": {"density": 12500, "name": "Seoul"},
        "+65": {"density": 1280, "name": "Singapore"},
        "+62": {"density": 1220, "name": "Jakarta"},
        "+92": {"density": 1600, "name": "Pakistan"},
    }

    locations = []

    for country_code, properties in country_code_to_properties.items():
        try:
            # Fetch location details using the country name
            location = geolocator.geocode(properties["name"])
            if location:
                locations.append({
                    "lat": location.latitude,
                    "lon": location.longitude,
                    "density": properties["density"],
                    "name": properties["name"],
                })
            else:
                print(f"Could not find location for {properties['name']}")
        except Exception as e:
            print(f"Error fetching location for {properties['name']}: {e}")

    return {"locations": locations}
