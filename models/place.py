#!/usr/bin/python3
"""
    A python Place Module
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
        Place Class for data Mangment
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
    amenity_ids = ""

    def to_dict(self):
        content = super().to_dict()
        content["city_id"] = Place.city_id
        content["user_id"] = Place.user_id
        content["name"] = Place.name
        content["description"] = Place.description
        content["number_rooms"] = Place.number_rooms
        content["number_bathrooms"] = Place.number_bathrooms
        content["max_guest"] = Place.max_guest
        content["price_by_night"] = Place.price_by_night
        content["latitude"] = Place.latitude
        content["amenity_ids"] = Place.amenity_ids
        return content
