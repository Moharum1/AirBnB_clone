#!/usr/bin/python3
"""
    A python Amenity Module
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity Class for data Mangment
    """

    def __init__(self, **kwargs):
        self.name = ""
        super().__init__(**kwargs)

    def to_dict(self):
        content = super().to_dict()
        content["name"] = self.name
        return content
