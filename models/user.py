#!/usr/bin/python3
"""
User module
Defines a User class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
