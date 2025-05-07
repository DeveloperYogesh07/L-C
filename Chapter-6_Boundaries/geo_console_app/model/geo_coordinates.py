class GeoCoordinates:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Latitude: {self.latitude}\nLongitude: {self.longitude}"
