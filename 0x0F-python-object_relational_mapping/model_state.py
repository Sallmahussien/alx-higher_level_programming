#!/usr/bin/python3
"""Contains the class definition of a State
   and an instance Base = declarative_base():
   """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state table for a MySQL database."""
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
