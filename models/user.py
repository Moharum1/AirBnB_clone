#!/usr/bin/python3
"""
    A python User Module
"""
from .base_model import BaseModel


class User(BaseModel):
    """
        User Class for data Mangment
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""


    def to_dict(self):
        content = super().to_dict()
        content["email"] = User.email
        content["password"] = User.password
        content["first_name"] = User.first_name
        content["last_name"] = User.last_name
        return content
