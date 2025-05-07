import requests
from model.geo_coordinates import GeoCoordinates
from service.geocoding_service import GeocodingService
from config import GEOCODE_MAPS_API_KEY


class GoogleGeocodingService(GeocodingService):
    def get_coordinates(self, location: str) -> GeoCoordinates:
        endpoint = "https://geocode.maps.co/search"
        params = {"q": location, "api_key": GEOCODE_MAPS_API_KEY}

        try:
            response = requests.get(endpoint, params=params, timeout=10)

            if response.status_code != 200:
                print(f"HTTP error: {response.status_code}")
                return None

            data = response.json()

            if not data or not isinstance(data, list):
                print("No results found for the given location.")
                return None

            lat = data[0].get("lat")
            lon = data[0].get("lon")

            if not lat or not lon:
                print("Latitude or Longitude not found in the response.")
                return None

            return GeoCoordinates(float(lat), float(lon))

        except requests.RequestException as e:
            print(f"Network error occurred: {e}")
            return None
        except (KeyError, IndexError, ValueError) as e:
            print(f"Data parsing error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
