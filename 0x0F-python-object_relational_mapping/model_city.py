#!/usr/bin/python3
"""Definition of city model"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", ForeignKey(State.id))
