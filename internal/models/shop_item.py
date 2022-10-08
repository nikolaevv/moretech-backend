from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship

from pkg.db.db import Base

class ShopItem(Base):
    __tablename__ = "shopitem"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    name = Column(Text, nullable=False)
    rarity = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    nft_items = relationship("NFTItem", back_populates="shop_item")