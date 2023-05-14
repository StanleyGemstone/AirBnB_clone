#!/usr/bin/python3
"""Test cases for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """implementing the test cases"""

    def test_init_(self):
        """test for correct instances initialization"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        obj_2.My_name = "Alx student"
        obj_2.My_cohort = 11
        time = datetime.now()
        self.assertNotEqual(obj_1.id, obj_2.id)
        self.assertNotEqual(time, obj_1.created_at)
        self.assertNotEqual(time, obj_2.created_at)
        self.assertEqual(type(obj_1.id), str)
        self.assertNotEqual(obj_1.created_at, obj_2.created_at)
        self.assertIsInstance(obj_1, BaseModel)
        # task 4 testcases
        get_dict = obj_2.to_dict()
        obj_3 = BaseModel(**get_dict)
        self.assertEqual(type(obj_3.created_at), datetime)
        self.assertEqual(type(obj_3.updated_at), datetime)
        self.assertNotIn("__class__", self.__dict__.keys())
        self.assertFalse(obj_2 is obj_3)
        self.assertIsInstance(obj_3, type(obj_2))

    def test_str(self):
        """Test for BaseModel __str__ method"""
        # task 3 testcases
        obj_1 = BaseModel()
        obj_1.name = "My First Model"
        obj_1.my_number = 89
        temp = type(obj_1).__name__
        copy = obj_1.to_dict().copy()
        del copy['__class__']
        flag1 = "[{}] ({}) {}".format(temp, obj_1.id, copy)
        flag2 = obj_1.__str__()
        self.assertTrue(flag1 == flag2)

    def test_save(self):
        """ test for save method of BaseModel Class"""
        # task 3 testcases
        obj = BaseModel()
        time = obj.updated_at
        obj.save()
        time2 = obj.updated_at
        self.assertNotEqual(time, time2)

    def test_to_dict(self):
        """test for to_dict method of the BaseModel Class"""
        # task 3 testcases
        obj = BaseModel()
        obj.name = "My Second Model"
        obj.my_number = 100
        dic = obj.to_dict()
        tup = ("id", "created_at", "updated_at", "__class__", "name")
        for keys, vals in dic.items():
            if (keys != "my_number"):
                self.assertIn(keys, tup)
                self.assertEqual(type(vals), str)
            else:
                self.assertEqual(type(vals), int)
