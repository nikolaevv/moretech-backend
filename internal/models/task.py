from __future__ import absolute_import
import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base

user_groups_table = Table(
    "user_groups",
    Base.metadata,
    Column("group_id", ForeignKey("group.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)

class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    assigner_id = Column(Integer, ForeignKey("users.id"))
    assigner = relationship("User", back_populates="tasks")
    
class Group(Base):
    __tablename__ = "group"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    members = relationship(
        "User", secondary=user_groups_table, back_populates="groups"
    )

class NFTItemType(enum.Enum):
    ITEM = "ITEM"
    PET = "PET"

class NFTItem(Base):
    __tablename__ = "nftitem"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    transaction_hash = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    type = Column(Enum(NFTItemType), default=NFTItemType.ITEM, nullable=False)
    shop_item_id = Column(Integer, ForeignKey("shopitem.id"))
    shop_item = relationship("ShopItem", back_populates="nft_items")
    pet_owner = relationship("User", back_populates="pet")
    nft_owner_id = Column(Integer, ForeignKey("users.id"))
    nft_owner = relationship("User", back_populates="inventory")

class ShopItem(Base):
    __tablename__ = "shopitem"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    name = Column(Text, nullable=False)
    rarity = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    nft_items = relationship("NFTItem", back_populates="shop_item")

class Transaction(Base):
    __tablename__ = "transaction"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    ended_at = Column(DateTime, nullable=False)

class RoleType(enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    DEVELOPER = "DEVELOPER"
    HR = "HR"

class User(Base):
    __tablename__ = "users"
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
    public_key = Column(Text, nullable=False)
    private_key = Column(Text, nullable=False)
    pet = relationship("NFTItem", back_populates="pet_owner", uselist=False)
    inventory = relationship("NFTItem", back_populates="nft_owner")
    tasks = relationship("Task", back_populates="assigner")
    groups = relationship(
        "Group", secondary=user_groups_table, back_populates="members"
    )

