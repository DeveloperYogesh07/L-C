from abc import ABC, abstractmethod
from model.geo_coordinates import GeoCoordinates

class GeocodingService(ABC):
    @abstractmethod
    def get_coordinates(self, location: str) -> GeoCoordinates:
        pass
