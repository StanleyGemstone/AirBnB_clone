#!/usr/bin/python3
"""A State is a subclass of BaseModel class"""

from models.base_model import BaseModel


class State(BaseModel):
    """The state class contains attr name"""
    name = ''
