#!/usr/bin/python3
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Subcategory(BaseModel, Base):
    """Representation of Review """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'subcategory'
        id = Column(String(128), primary_key=True)
        userId = Column(String(128), ForeignKey('user.id'))
        name = Column(String(128))
        categoryId = Column(String(128), ForeignKey('category.id'))
        limit = Column(Float)

        user = relationship('User', back_populates='subcategories')
        category = relationship('Category', back_populates='subcategories')
        entries = relationship('Entry', back_populates='subcategory')
    else:
        userId = ""
        name = ""
        categoryId = ""
        limit = 0.0

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
