#!/usr/bin/python3
"""
    A python User Module
"""
from .base_model import BaseModel
class User(BaseModel):
    """
        User Class for data Mangment
    """

    def __init__(self, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(**kwargs)

    def to_dict(self):
        content = super().to_dict()
        content["email"] = self.email
        content["password"] = self.password
        content["first_name"] = self.first_name
        content["last_name"] = self.last_name
        return content

