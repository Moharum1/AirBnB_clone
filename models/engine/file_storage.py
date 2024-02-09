#!/usr/bin/python3
"""
    A file storage class to handle conversion from and to JSON objects
"""
import json
import os

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
        with open(self.__file_path, "w") as localStorage:
            json.dump(self.__objects, localStorage)

    def reload(self):
        """
        Checks if there is a json file in the path
            if exist extract all the objects from it
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as localStorage:
                self.__objects = json.load(localStorage)
    
    def delete(self, id):
        """
            remove an object from the Storage

            Args:
                id (str) : unique id of the obj in the format <class_name>.<obj.id>
        """
        if id in self.__objects:
            self.__objects.pop(id)
            self.save()