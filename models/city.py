#!/usr/bin/python3
"""
    A python City Module
"""
from .base_model import BaseModel


class City(BaseModel):
    """
        City Class for data Mangment
    """

    def __init__(self, **kwargs):
        self.name = ""
        self.state_id = ""
        super().__init__(**kwargs)

    def to_dict(self):
        content = super().to_dict()
        content["name"] = self.name
        content["state_id"] = self.state_id
        return content
