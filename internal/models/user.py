import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship
from .associations import user_groups_table

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
    pet = relationship("NFTItem", back_populates="pet_owner", uselist=False)
    inventory = relationship("NFTItem", back_populates="nft_owner")
    power = Column(Integer, default=0)
    work_adress = Column(Text, nullable=False)
    temp_power = Column(Integer, default=0)
    balance = Column(Float, default=0.0)
    groups = relationship(
        "Group", secondary=user_groups_table, back_populates="members"
    )
    gitlab_token = Column(Text, nullable=False)
    