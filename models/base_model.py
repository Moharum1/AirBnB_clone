#!/usr/bin/python3
"""
    A python Base model class
"""
import uuid
import models
from datetime import datetime


class BaseModel():
    """
        Abstract class containing the main function needed to
            Store, delete, edit and show Data in the database
    """

    def __init__(self, *args, **kwargs):
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
            self.updated_at = self.created_at
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)

    def save(self):
        """ Updates the content of the Storage file"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        A function that return a dict with:
            - The object public members
            - The name of the class
        """
        my_dict = {**self.__dict__}
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    @classmethod
    def all(cls):
        """
            return The String representation of all object
            having the same name in Storage as the caller class
        """
        items = []
        AvailableObj = models.storage.all()
        for key, val in AvailableObj.items():
            if cls.__name__ in key:
                items.append(str(val))
        print(items)

    @classmethod
    def count(cls):
        """
            return the number of Objects inside
            the Storage which has the same type as Caller Object
        """
        count = 0
        AvailableObj = models.storage.all()
        for key, _ in AvailableObj.items():
            if cls.__name__ in key:
                count += 1
        print(count)

    @classmethod
    def show(cls, id):
        """
            show the content of the class
        """
        classKey = "{}.{}".format(cls.__name__, id)
        AvilableObj = models.storage.all()

        if classKey in AvilableObj:
            print(AvilableObj[classKey].__str__())
        else:
            print("** no instance found **")

    @classmethod
    def destroy(cls, id):
        """
            destroy the object from Storage
        """
        classKey = "{}.{}".format(cls.__name__, id)
        AvilableObj = models.storage.all()

        if classKey in AvilableObj:
            models.storage.delete(classKey)
        else:
            print("** no instance found **")

    def __str__(self):
        """
        return a string containing :
            - The class name
            - The id of the object
            - A dict for the object public members
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
