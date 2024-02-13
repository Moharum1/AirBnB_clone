#!/usr/bin/python3
"""
    A file storage class to handle conversion from and to JSON objects
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
            a function that return a dict containing all the avilable BaseModel objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        Add a new object into the file Storage
            The key for your object will be <Class name>.<object.id>

        Args:
            obj (BaseModel) : object you want to add to storage
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Save the current avilable objects into a JSON file
        """
        serialized = {
            key: val
            for key, val in self.__objects.items()
        }
        with open(self.__file_path, "w") as localStorage:
            json.dump(serialized, localStorage)

    def reload(self):
        """
        Checks if there is a json file in the path
            if exist extract all the objects from it
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as localStorage:
                deserialize = json.load(localStorage)
                self.__objects = {
                    key: eval(obj["__class__"])(**obj)
                    for key, obj in deserialize.items()}
    
    def delete(self, id):
        """
            remove an object from the Storage

            Args:
                id (str) : unique id of the obj in the format <class_name>.<obj.id>
        """
        if id in self.__objects:
            self.__objects.pop(id)
            self.save()