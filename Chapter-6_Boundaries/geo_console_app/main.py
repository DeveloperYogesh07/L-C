from service.google_geocoding_service import GoogleGeocodingService

def main():
    location = input("Enter a place: ").strip()
    geocoder = GoogleGeocodingService()
    coordinates = geocoder.get_coordinates(location)

    if coordinates:
        print(coordinates)
    else:
        print("Could not retrieve coordinates.")

if __name__ == "__main__":
    main()
