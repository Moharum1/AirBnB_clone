#!/usr/bin/python3
"""
    A python Place Module
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
        Place Class for data Mangment
    """

    def __init__(self, **kwargs):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = ""
        super().__init__(**kwargs)

    def to_dict(self):
        content = super().to_dict()
        content["city_id"] = self.city_id
        content["user_id"] = self.user_id
        content["name"] = self.name
        content["description"] = self.description
        content["number_rooms"] = self.number_rooms
        content["number_bathrooms"] = self.number_bathrooms
        content["max_guest"] = self.max_guest
        content["price_by_night"] = self.price_by_night
        content["latitude"] = self.latitude
        content["amenity_ids"] = self.amenity_ids
        return content
