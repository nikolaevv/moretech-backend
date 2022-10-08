from __future__ import absolute_import
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

from pkg.db.db import Base

class TaskAssign(Base):
    __tablename__ = "taskassign"
    id = Column(Integer, primary_key=True, index=True)
    done = Column(Boolean, nullable=False)