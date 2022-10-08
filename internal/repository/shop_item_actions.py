from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import Shopitem
from internal.schemas.schemas import ShopItemCreate


def get_shopitems(db: Session) -> list[Shopitem]:
    return db.query(Shopitem).all()

def get_shopitem_by_id(db: Session, id: int) -> Shopitem:
    shopitems = db.query(Shopitem).filter(Shopitem.id == id)
    if shopitems.count() > 0:
        return shopitems.first()

def create_shopitem(db: Session, shop_item: ShopItemCreate) -> None:
    db_object = Shopitem(**shop_item.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)