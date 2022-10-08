from __future__ import absolute_import
import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base

class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    
class Group(Base):
    __tablename__ = "group"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)

class NFTItemType(enum.Enum):
    ITEM = "ITEM"
    PET = "PET"

class NFTItem(Base):
    __tablename__ = "nftitem"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    type = Column(Enum(NFTItemType), default=NFTItemType.ITEM, nullable=False)

class ShopItem(Base):
    __tablename__ = "shopitem"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    name = Column(Text, nullable=False)
    rarity = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)

class TaskAssign(Base):
    __tablename__ = "taskassign"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    done = Column(Boolean, nullable=False)

class Transaction(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    ended_at = Column(DateTime, nullable=False)

class RoleType(enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    DEVELOPER = "DEVELOPER"
    HR = "HR"

class User(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    login = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    token = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    role = Column(Enum(RoleType), default=RoleType.DEVELOPER, nullable=False)
    power = Column(Integer, default=0)
    work_adress = Column(Text, nullable=False)
    temp_power = Column(Integer, default=0)
    balance = Column(Float, default=0.0)
    gitlab_token = Column(Text, nullable=False)