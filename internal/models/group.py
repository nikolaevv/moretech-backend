from __future__ import absolute_import
from sqlalchemy import Column, Integer, Table, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship
from .associations import user_groups_table

from pkg.db.db import Base

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    members = relationship(
        "User", secondary=user_groups_table, back_populates="groups"
    )
