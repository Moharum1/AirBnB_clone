#!/usr/bin/python3
"""
    A python State Module
"""
from .base_model import BaseModel


class State(BaseModel):
    """
        State Class for data Mangment
    """

    # Atrributes
    name: str = ''

    def to_dict(self):
        content = super().to_dict()
        content["name"] = State.name
        return content
