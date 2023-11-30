#!/usr/bin/python3
""" holds class entry"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Entry(BaseModel, Base):
    """Representation of entry """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'entry'
        id = Column(String(128), primary_key=True)
        userId = Column(String(128), ForeignKey('user.id'))
        amount = Column(Float)
        comment = Column(String(128))
        categoryId = Column(String(128), ForeignKey('category.id'))
        subcategoryId = Column(String(128), ForeignKey('subcategory.id'))
        timestamp = Column(DateTime)

        user = relationship('User', back_populates='entries')
        category = relationship('Category', back_populates='entries')
        subcategory = relationship('Subcategory', back_populates='entries')
    else:
        userId = ""
        amount = 0
        comment = ""
        categoryId = ""
        subcategoryId = ""
        timestamp = 0

    def __init__(self, *args, **kwargs):
        """initializes entry"""
        super().__init__(*args, **kwargs)
