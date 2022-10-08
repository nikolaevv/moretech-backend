from __future__ import absolute_import
from http.client import HTTPException
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Dict
import bcrypt

from internal.schemas.schemas import *
from internal.repository.user_actions import *
from pkg.db.db import SessionLocal, Base, engine


Base.metadata.create_all(bind=engine)

routes = APIRouter(
    prefix='/api'
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@routes.post("/auth", status_code=201)
def auth(login: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_login(db, login)
    
    if not user:
        raise HTTPException(status_code=401, detail='User not found')
    pwd = password.encode(encoding = 'UTF-8', errors = 'strict')
    cur_pwd = get_pwd_by_login(db, login).encode(encoding = 'UTF-8', errors = 'strict')
    if not bcrypt.checkpw(pwd, cur_pwd):
        raise HTTPException(status_code=403, detail='Wrong password')
    return auth_user(db, user)


@routes.get("/shopitem", status_code=200)
def get_shopitem(db: Session = Depends(get_db)) -> None:
    pass

@routes.post("/shopItem/{id}/buy", status_code=201)
def buy_shop_item(id: int, db: Session = Depends(get_db)) -> None:
    pass

@routes.get("/nftItem", status_code=200)
def get_nft_item(db: Session = Depends(get_db)) -> None:
    pass

@routes.put("/nftItem/transfer", status_code=200)
def transfer_nft_item(db: Session = Depends(get_db)) -> None:
    pass

@routes.get("/user/{id}", status_code=200)
def get_user_by_id(id: int, db: Session = Depends(get_db)) -> None:
    pass

@routes.get("/user/{id}/transaction", status_code=200)
def get_user_transaction_by_id(id: int, db: Session = Depends(get_db)) -> None:
    pass

@routes.get("/user", status_code=200)
def get_user_by_params(group_id: int, db: Session = Depends(get_db)) -> None:
    pass

@routes.get("/stat", status_code=200)
def get_statistics(db: Session = Depends(get_db)) -> None:
    pass

