from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import Nftitem
from internal.schemas.schemas import NFTItemCreate


def get_nftitems(db: Session) -> list[Nftitem]:
    return db.query(Nftitem).all()

def get_nftitem_by_id(db: Session, id: int) -> Nftitem:
    nftitems = db.query(Nftitem).filter(Nftitem.id == id)
    if nftitems.count() > 0:
        return nftitems.first()

def create_nftitem(db: Session, nftItem: NFTItemCreate) -> None:
    db_object = Nftitem(**nftItem.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)