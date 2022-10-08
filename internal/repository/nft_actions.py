from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import NFTItem
from internal.schemas.schemas import NFTItemCreate


def get_nftitems(db: Session) -> list[NFTItem]:
    return db.query(NFTItem).all()

def get_nftitem_by_id(db: Session, id: int) -> NFTItem:
    nftitems = db.query(NFTItem).filter(NFTItem.id == id)
    if nftitems.count() > 0:
        return nftitems.first()

def get_nftitem_by_user_id(db: Session, user_id: int) -> NFTItem:
    nftitems = db.query(NFTItem).filter(NFTItem.nft_owner_id == user_id)
    if nftitems.count() > 0:
        return nftitems.first()

def create_nftitem(db: Session, nftItem: NFTItemCreate) -> None:
    db_object = NFTItem(**nftItem.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)

def update_nftitem(db: Session, nftItem: NFTItemCreate):
    db.add(nftItem)
    db.commit()
    db.refresh(nftItem)
    return nftItem