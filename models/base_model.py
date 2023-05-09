#!/usr/bin/python3
"""BaseModel class defines all common attributes/methods
    for other classes in the Airbnb package
"""

import uuid
import datetime


class BaseModel:
    """BaseModel class definition"""

    def __init__(self):
        """handle initiliazaton of the class instances"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return the unofficial string representation for class instances"""
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dictionary containing all
            keys/values of __dict__ of the instance
            plus addition __class__ key with value correspond
            to the class name of the instances:
        """
        ret_dict = self.__dict__
        ret_dict['created_at'] = self.created_at.isoformat()
        ret_dict['updated_at'] = self.updated_at.isoformat()
        ret_dict['__class__'] = type(self).__name__
        return ret_dict
