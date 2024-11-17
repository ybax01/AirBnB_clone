#!/usr/bin/python3
"""
BaseModel module for the base class of the project.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for other models.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Time of creation.
        updated_at (datetime): Time of last update.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute and saves to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary representation.
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """
        Returns the string representation of the instance.

        Returns:
            str: String representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
