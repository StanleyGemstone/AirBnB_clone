#!/usr/bin/python3
"""City is a subclass of BaseModel class"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City class contains attr name and state_id"""
    state_id = ''
    name = ''
