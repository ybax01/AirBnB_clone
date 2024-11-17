#!/usr/bin/python3
"""
Amenity module containing the Amenity class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
