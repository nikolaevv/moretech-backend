from __future__ import absolute_import
from pydantic import BaseModel
from datetime import datetime
from internal.models.task import RoleType, NFTItemType

# Task schema
class TaskBase(BaseModel):
    text: str
    created_at: datetime
    
class TaskCreate(TaskBase):
    assigner_id: int

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


# ShopItem schema
class ShopItemBase(BaseModel):
    price: float
    name: str
    rarity: str
    description: str
    
class ShopItemCreate(ShopItemBase):
    pass

class ShopItem(ShopItemBase):
    id: int

    class Config:
        orm_mode = True


# NFTItem schema
class NFTItemBase(BaseModel):
    name: str
    price: float
    shop_item: ShopItem
    type: NFTItemType = NFTItemType.ITEM
    
class NFTItemCreate(NFTItemBase):
    pass

class NFTItem(NFTItemBase):
    id: int

    class Config:
        orm_mode = True


# Group schema
class GroupBase(BaseModel):
    name: str
    
class GroupCreate(GroupBase):
    pass


# User schema
class UserBase(BaseModel):
    login: str
    token: str
    name: str
    role: RoleType = RoleType.DEVELOPER
    power: int = 0.0
    work_address: str
    temp_power: int = 0.0
    balance: float = 0.0
    gitlab_token: str
    private_key: str
    public_key: str

class UserAuth(UserBase):
    password_hash: str

# User - Group schemas
class Group(GroupBase):
    id: int
    members: list[UserBase] = []

    class Config:
        orm_mode = True



class User(UserBase):
    id: int
    pet: NFTItem
    inventory: list[NFTItem] = []
    groups: list[GroupBase] = []

    class Config:
        orm_mode = True


# Transaction schema
class TransactionBase(BaseModel):
    ended_at: datetime = None
    sender: User
    receiver: User
    
class TransactionCreate(BaseModel):
    sender_id: int
    receiver_id: int

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True