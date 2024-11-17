#!/usr/bin/python3
"""
Review module containing the Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): The ID of the place the review is for.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
