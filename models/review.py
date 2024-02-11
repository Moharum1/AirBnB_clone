#!/usr/bin/python3
"""
    A python review Module
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
        Review Class for data Mangment
    """

    def __init__(self, **kwargs):
        self.text = ""
        self.place_id = ""
        self.user_id = ""
        super().__init__(**kwargs)

    def to_dict(self):
        content = super().to_dict()
        content["name"] = self.name
        content["place_id"] = self.place_id
        content["user_id"] = self.user_id
        return content
