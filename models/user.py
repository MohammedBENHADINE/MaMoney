#!/usr/bin/python3
""" holds class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Representation of a user """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'user'
        id = Column(String(128), primary_key=True)
        email = Column(String(128))
        username = Column(String(128))
        _password = Column(String(128))
        profileDetails = Column(String(128))

        entries = relationship('Entry', back_populates='user')
        settings = relationship('Settings',uselist=False, back_populates='user')
        categories = relationship('Category',back_populates='user')
        subcategories = relationship('Subcategory',back_populates='user')
    else:
        id = ""
        email = ""
        _password = ""
        username = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """hashing password values"""
        self._password = hashlib.md5(pwd.encode()).hexdigest()
