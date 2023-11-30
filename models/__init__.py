#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv

# DBSTORAGE
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
storage.reload()