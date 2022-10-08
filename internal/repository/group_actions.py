from __future__ import absolute_import
from tkinter import N
from sqlalchemy.orm import Session
from internal.models.group import Group
from internal.schemas.schemas import GroupCreate


def get_groups(db: Session) -> list[Group]:
    return db.query(Group).all()

def get_group_by_id(db: Session, id: int) -> Group:
    groups = db.query(Group).filter(Group.id == id)
    if groups.count() > 0:
        return groups.first()

def create_group(db: Session, group: GroupCreate) -> None:
    db_object = Group(**group.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)