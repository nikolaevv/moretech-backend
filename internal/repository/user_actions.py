from __future__ import absolute_import
from typing import List
from sqlalchemy.orm import Session
from internal.models.task import User, Group
from internal.schemas.schemas import UserAuth
import uuid
import requests

base_url = 'https://hackathon.lsp.team/hk'

def create_tokens():
    r = requests.post('{}/v1/wallets/new'.format(base_url))
    return r.json()

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

def get_users_by_group(db: Session, id: int) -> List[User]:
    return db.query(User).filter(
        User.groups.any(Group.Id == id)
    )

def get_user_by_id(db: Session, id: int) -> User:
    users = db.query(User).filter(User.id == id)
    if users.count() > 0:
        return users.first()

def auth_user(db: Session, user: User):
    user.token = uuid.uuid4()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user