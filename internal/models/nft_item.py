from __future__ import absolute_import
import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base

class NFTItemType(enum.Enum):
    ITEM = "ITEM"
    PET = "PET"

class NFTItem(Base):
    __tablename__ = "nftitem"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    type = Column(Enum(NFTItemType), default=NFTItemType.ITEM, nullable=False)
    shop_item_id = Column(Integer, ForeignKey("shop_item.id"))
    shop_item = relationship("ShopItem", back_populates="nft_item")
    pet_owner = relationship("User", back_populates="pet")
    item_owner_id = Column(Integer, ForeignKey("inventory.id"))
    item_owner = relationship("User", back_populates="item")