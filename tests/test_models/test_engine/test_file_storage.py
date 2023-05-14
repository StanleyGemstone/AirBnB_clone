#!/usr/bin/python3
"""Different cases for file_storage engine module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """The file storage module contain methods for storing, writing,
    reading,and converting, json data and the package objects - i.e.
    serialization and deserialization.
    """
    container = FileStorage()

    def test_all(self):
        """Testing if the all() return object of type dictionary"""

        self.assertTrue(type(self.container.all()), dict)

    def test_new(self):
        """
        *Testing for proper key naming requirement <class name.id>
        """
        dic = dict(self.container.all())
        if dic is not None:
            for keys, val in dic.items():
                name = "{}.{}".format(str(type(val).__name__), val.id)
                self.assertTrue(keys == name)

    def test_new_obj(self):
        """*Testing if the key value is an
        object of class or subclass BaseModel
        """
        dic = dict(self.container.all())
        if dic is not None:
            for keys, val in dic.items():
                self.assertIsInstance(val, BaseModel)

    def test_save(self):
        """testing save method of Filestorage class"""
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test if reload initialize __object of FileStorage attribute
        """
        pass
