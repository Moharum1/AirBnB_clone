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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            a function that return a dict containing all the avilable BaseModel objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Add a new object into the file Storage
            The key for your object will be <Class name>.<object.id>

        Args:
            obj (BaseModel) : object you want to add to storage
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Save the current avilable objects into a JSON file
        """
        serialized = {
            key: val.to_dict()
            for key, val in FileStorage.__objects.items()
        }
        with open(self.__file_path, "w") as localStorage:
            json.dump(serialized, localStorage)

    def reload(self):
        """
        Checks if there is a json file in the path
            if exist extract all the objects from it
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as localStorage:
                deserialize = json.load(localStorage)
                FileStorage.__objects = {
                    key: eval(obj["__class__"])(**obj)
                    for key, obj in deserialize.items()}
    
    def delete(self, id):
        """
            remove an object from the Storage

            Args:
                id (str) : unique id of the obj in the format <class_name>.<obj.id>
        """
        for key,value in FileStorage.__objects.items():
            if key == id:
                del FileStorage.__objects[key]
                self.save()
                break