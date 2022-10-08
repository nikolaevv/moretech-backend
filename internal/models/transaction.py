import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base


class Transaction(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    ended_at = Column(DateTime, nullable=False)
    sender_id = Column(Integer, ForeignKey("user.id"))
    receiver_id = Column(Integer, ForeignKey("user.id"))