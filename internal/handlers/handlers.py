from __future__ import absolute_import
from http.client import HTTPException
import random
from uuid import uuid4
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Dict, List
import bcrypt
from datetime import datetime

from internal.schemas.schemas import *
from internal.repository.shop_item_actions import *
from internal.repository.user_actions import *
from internal.repository.transactions import *
from internal.repository.nft_actions import *
from internal.repository.task_actions import *

from pkg.db.db import SessionLocal, Base, engine
from pkg.db.tasks import tasks
from pkg.blockchain.api import create_nft

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
    return get_shopitems(db)

@routes.post("/shopItem/{id}/buy", status_code=201)
def buy_shop_item(id: int, user_id: str, nf: NFTItemCreate, db: Session = Depends(get_db)) -> None:
    create_nftitem(db, nf)
    user = get_user_by_id(user_id)
    data = create_nft(id, user.public_key)

    nft_item = get_nftitem_by_id(db, id)
    if nft_item.nft_owner_id == transaction.sender_id:
        raise HTTPException(status_code=403, detail='You do not have permission for action')
    nft_item.transaction_hash = data['transactionHash']
    update_nftitem(db, nft_item)

@routes.get("/nftItem", status_code=200)
def get_nft_item(user_id: int, db: Session = Depends(get_db)) -> None:
    return get_nftitem_by_user_id(db, user_id)

@routes.put("/nftItem/{id}/transfer", status_code=200)
def transfer_nft_item(id: int, transaction: TransactionCreate, db: Session = Depends(get_db)) -> None:
    # 1. Менять у нфт владельца
    nft_item = get_nftitem_by_id(db, id)
    if nft_item.nft_owner_id == transaction.sender_id:
        raise HTTPException(status_code=403, detail='You do not have permission for action')

    nft_item.nft_owner_id = transaction.receiver_id
    update_nftitem(db, nft_item)
    # 2. Создать транзакцию
    create_transaction(db, transaction)

@routes.get("/user/{id}", status_code=200)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, id)

@routes.get("/user/{id}/transaction", status_code=200)
def get_user_transaction_by_id(id: int, db: Session = Depends(get_db)) -> None:
    return get_transactions_by_user_id(db, id)

@routes.get("/user", status_code=200)
def get_user_by_params(group_id: int, db: Session = Depends(get_db)) -> List[User]:
    return get_users_by_group(db, group_id)

@routes.get("/stat", status_code=200)
def get_statistics(db: Session = Depends(get_db)) -> None:
    return {}

@routes.post("/task", status_code=201)
def create_user_task(user_id: int, db: Session = Depends(get_db)) -> None:
    task_text = random.choice(tasks)
    create_task(db, TaskCreate(text=task_text, assigner_id=user_id, created_at=datetime.now()))
    return {'task': task_text}


#admin_routes = APIRouter(
#    prefix='/add'
#)
#@admin_routes.post("/user", status_code=201)
#def create_user(
#     login: str, pwd: str, name: str, gitlab_token: str, work_address: str,
#     db: Session = Depends(get_db)
#):
#    access_token = str(uuid4())
#    pwd_hash = str(pwd.encode(encoding = 'UTF-8', errors = 'strict'))
#    print(pwd_hash)
#    tokens = create_tokens()
#    public_key = tokens["publicKey"]
#    private_key = tokens["privateKey"]
#    print(public_key)
#    print(private_key)
#    user = UserAuth(
#        login=login, token=access_token, name=name, role=RoleType.DEVELOPER, work_address=work_address,
#        gitlab_token=gitlab_token, private_key=private_key, public_key=public_key,
#        password_hash=pwd_hash
#    )
#    db.add(user)
#    db.commit()
#    db.refresh(user)
#    return user