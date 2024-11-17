#!/usr/bin/python3
"""
Place module containing the Place class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): The ID of the city the place belongs to.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests allowed.
        price_by_night (int): Price per night to stay at the place.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        amenity_ids (list of str): List of Amenity IDs associated with the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
