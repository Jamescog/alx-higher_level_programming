#!/usr/bin/python3
"""
    contain the defination of Model(Base) class for sqlalchemy
"""


from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, MetaData

myMetadata = MetaData()
Base = declarative_base(metadata=myMetadata)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
