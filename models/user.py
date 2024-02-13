#!/usr/bin/python3
"""
    A python User Module
"""
from .base_model import BaseModel


class User(BaseModel):
    """
        User Class for data Mangment
    """
    
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''

    def to_dict(self):
        new_dict = super().to_dict()
        new_dict["email"] = User.email
        new_dict["password"] = User.password
        new_dict["first_name"] = User.first_name
        new_dict["last_name"] = User.last_name
        return new_dict
    
