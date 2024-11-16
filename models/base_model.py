#!/usr/bin/python3
"""
BaseModel module defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Defines the BaseModel class with common attributes and methods.

    Attributes:
        id (str): Unique id assigned to each instance (UUID4).
        created_at (datetime): Datetime when an instance is created.
        updated_at (datetime): Datetime updated whenever the object changes.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__.
        Adds the __class__ key with the class name.
        Converts created_at and updated_at to ISO 8601 format strings.

        Returns:
            dict: Dictionary representation of the instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
