#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as a base class
for other models. It includes common attributes and methods.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        - If kwargs is provided and not empty, it creates attributes
          from the key-value pairs in kwargs (except '__class__').
        - Otherwise, it generates a new id and sets created_at and updated_at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
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
        Updates the public instance attribute `updated_at`
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        - Includes all attributes in __dict__.
        - Adds a `__class__` key with the class name.
        - Converts created_at and updated_at to ISO format strings.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
