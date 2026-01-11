#!/usr/bin/python3
"""
Module that defines the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the base model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    try:
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    except ValueError:
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                    setattr(self, key, val)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            import models
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime and saves the instance to storage
        """
        self.updated_at = datetime.now()
        import models
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
