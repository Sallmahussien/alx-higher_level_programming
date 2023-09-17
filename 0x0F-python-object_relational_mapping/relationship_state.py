#!/usr/bin/python3
"""Definition of city model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents a state table for a MySQL database."""
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
