#!/usr/bin/python3
"""Test cases for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """implementing the test cases"""

    def test_init_BM(self):
        """test for correct instance initialization"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        time = datetime.now()
        self.assertNotEqual(obj_1.id, obj_2.id)
        self.assertNotEqual(time, obj_1.created_at)
        self.assertNotEqual(time, obj_2.created_at)
        self.assertEqual(type(obj_1.id), str)
        self.assertNotEqual(obj_1.created_at, obj_2.created_at)
        self.assertIsInstance(obj_1, BaseModel)

    def test_str(self):
        """Test for BaseModel __str__ method"""
        obj_1 = BaseModel()
        obj_1.name = "My First Model"
        obj_1.my_number = 89
        temp = type(obj_1).__name__
        flag1 = "[{}] ({}) {}".format(temp, obj_1.id, obj_1.__dict__)
        flag2 = obj_1.__str__()
        self.assertTrue(flag1 == flag2)

    def test_save(self):
        """ test for save method of BaseModel Class"""
        obj = BaseModel()
        time = obj.updated_at
        obj.save()
        time2 = obj.updated_at
        self.assertNotEqual(time, time2)

    def test_to_dict(self):
        """test for to_dict method of the BaseModel Class"""
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
