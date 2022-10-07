from fastapi import APIRouter
from typing import List


routes = APIRouter()

@routes.post("/auth", status_code=201)
def auth(self) -> None:
    pass

@routes.get("/shopitem", status_code=200)
def get_shopitem() -> None:
    pass

@routes.post("/shopItem/{id}/buy", status_code=201)
def func() -> None:
    pass

@routes.get("/nftItem", status_code=200)
def get_nft_item() -> None:
    pass

@routes.put("/nftItem/transfer", status_code=200)
def transfer_nft_item() -> None:
    pass

@routes.get("/user/{id}", status_code=200)
def get_user_by_id() -> None:
    pass

@routes.get("/user/{id}/transaction", status_code=200)
def get_user_transaction_by_id() -> None:
    pass

@routes.get("/user", status_code=200)
def get_user_by_params(group_id:int) -> None:
    pass

@routes.get("/stat", status_code=200)
def get_statistics() -> None:
    pass