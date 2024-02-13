#!/usr/bin/python3
"""
    A python City Module
"""
from .base_model import BaseModel


class City(BaseModel):
    """
        City Class for data Mangment
    """

    name = ""
    state_id = ""

    def to_dict(self):
        content = super().to_dict()
        content["name"] = City.name
        content["state_id"] = City.state_id
        return content
