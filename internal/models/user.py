from __future__ import absolute_import
import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base

class RoleType(enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    DEVELOPER = "DEVELOPER"
    HR = "HR"

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    login = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    token = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    role = Column(Enum(RoleType), default=RoleType.DEVELOPER, nullable=False)
    pet = relationship("NFTItem")
    inventory = relationship("NFTItem")
    power = Column(Integer, default=0)
    work_adress = Column(Text, nullable=False)
    temp_power = Column(Integer, default=0)
    balance = Column(Float, default=0.0)
    gitlab_token = Column(Text, nullable=False)
    taskassign_id = Column(Integer, ForeignKey('taskassign.id'), nullable=True)
    