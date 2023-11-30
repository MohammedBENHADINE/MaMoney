#!/usr/bin/python3
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Settings(BaseModel, Base):
    """Representation of Settings """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'settings'
        id = Column(String(128), primary_key=True)
        userId = Column(String(128), ForeignKey('user.id'))
        spendingDuration = Column(String(128))
        startingDay = Column(String(128))
        userSettings = Column(String(128))

        user = relationship('User', back_populates='settings')
    else:
        userId = ""
        spendingDuration = ""
        startingDay = ""
        userSettings = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
