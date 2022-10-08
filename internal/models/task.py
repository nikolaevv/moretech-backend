from __future__ import absolute_import
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)