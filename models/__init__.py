#!/usr.bin/python3
"""creating a unique FileStorage instance for console application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
