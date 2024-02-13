#!/usr/bin/python3
"""
    A python review Module
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
        Review Class for data Mangment
    """

    # Attributes
    place_id: str = ''
    user_id: str = ''
    text: str = ''

    def to_dict(self):
        content = super().to_dict()
        content["name"] = Review.name
        content["place_id"] = Review.place_id
        content["user_id"] = Review.user_id
        return content
