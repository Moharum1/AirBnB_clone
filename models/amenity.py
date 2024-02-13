#!/usr/bin/python3
"""
    A python Amenity Module
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity Class for data Mangment
    """

    name = ''

    def to_dict(self):
        content = super().to_dict()
        content["name"] = Amenity.name
        return content
