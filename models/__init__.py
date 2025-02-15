#!/usr/bin/python3
"""Instance of the Storage"""

from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
