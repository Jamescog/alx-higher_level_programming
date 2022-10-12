#!/usr/bin/python3
"""
    contain the defination of Model(Base) class for sqlalchemy
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class State(Base):
    """
        maps to table states
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
