#!/usr/bin/python3
"""
    A python Base model class 
"""
import uuid
import json
from models import storage
from datetime import datetime


class BaseModel():

    def __init__(self, **kwargs):
        """
        A function called when initializing a class object
            Create an object with the following public attributes:
                id (int) : a unique id for each object
                created_at (datetime) : the time the object was created
                updated_at (datetime) : the time of the last edit of the object
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)

    def save(self):
        """
            Updates the content of the Storage file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        A function that return a dict with:
            - The object public members
            - The name of the class 
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
    
    @classmethod
    def all(self):
        items = []
        AvilableObj = storage.all()
        for key, val in AvilableObj.items():
            if self.__name__ in key:
                items.append(self(**val).__str__())
        print(items)

    def __str__(self):
        """
        return a string containing :
            - The class name
            - The id of the object
            - A dict for the object public members
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
