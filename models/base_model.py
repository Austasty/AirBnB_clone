#!/usr/bin/python3
"""base_model module"""
from models import storage
import uuid
from datetime import datetime



class BaseModel:
    """Definition of the BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """BaseModel Class constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] =\
                    datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v

        storage.new(self)

    def __str__(self) -> str:
        """Prints string representaion of a model"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
            * by using self.__dict__, only instance
            attributes set will be returned
            * a key __class__ must be added to this
            dictionary with the class name of the object
            * created_at and updated_at must be converted
            to string object in ISO format
        """
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        return object_dict
