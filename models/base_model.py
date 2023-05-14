#!/usr/bin/python3
"""BaseModel class defines all common attributes/methods
    for other classes in the Airbnb package
"""

import uuid
import datetime
from models import storage


class BaseModel:
    """BaseModel class definition"""

    def __init__(self, *args, **kwargs):
        """
        handle initiliazaton of the class instances using either empty init
        argument or non-keyword argumemt as list, or keyword argument as dict
        """

        if (kwargs):
            self.id = str(uuid.uuid4())
            tup = ("__class__", "created_at", "updated_at")
            for key, val in kwargs.items():
                if (key not in tup):
                    setattr(self, key, val)
                else:
                    if key == "created_at":
                        self.created_at = datetime.datetime.fromisoformat(val)
                    elif key == "updated_at":
                        self.updated_at = datetime.datetime.fromisoformat(val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """return the unofficial string representation for class instances"""
        # print("\n", self.__dict__, "\n")
        rm_class_key = dict(self.to_dict())
        del rm_class_key["__class__"]
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, rm_class_key)
        return s

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """
        storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dictionary containing all keys/values of __dict__
            of the instance plus addition __class__ key with value correspond
            to the class name of the instances
        """
        ret_dict = self.__dict__
        ret_dict['__class__'] = type(self).__name__
        for key in ret_dict.keys():
            if (type(ret_dict[key]) == datetime.datetime):
                ret_dict[key] = ret_dict[key].isoformat()
        return ret_dict
