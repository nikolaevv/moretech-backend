from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import User
from internal.schemas.schemas import UserAuth
import uuid


def get_user_by_login(db: Session, login: str) -> User | None:
    users = db.query(User).filter(User.login == login)
    if users.count() > 0:
        return users.first()

def get_pwd_by_login(db: Session, login: str) -> bytes | None:
    users = db.query(User).filter(User.login == login)
    if users.count() > 0:
        return users.first().password_hash

def get_users(db: Session) -> list[User]:
    return db.query(User).all()

def get_user_by_id(db: Session, id: int) -> User:
    users = db.query(User).filter(User.id == id)
    if users.count() > 0:
        return users.first()

def auth_user(db: Session, user: UserAuth) -> None:
    db_object = User(token=uuid.uuid4())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object