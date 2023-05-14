#!/usr/bin/python3
"""Review is a subclass of BaseModel class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""
    place_id = ''
    user_id = ''
    text = ''
