#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of state """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'category'
        id = Column(String(128), primary_key=True)
        userId = Column(String(128), ForeignKey('user.id'))
        name = Column(String(128))
        limit = Column(Float)

        user = relationship('User', back_populates='categories')
        subcategories = relationship('Subcategory', back_populates='category')
        entries = relationship('Entry', back_populates='category')
    else:
        name = ""
        userId = ""
        limit = 0.0

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
