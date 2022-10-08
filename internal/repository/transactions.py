from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import Transaction
from internal.schemas.schemas import TransactionCreate


def get_transactions(db: Session) -> list[Transaction]:
    return db.query(Transaction).all()

def get_transaction_by_id(db: Session, id: int) -> Transaction:
    transactions = db.query(Transaction).filter(Transaction.id == id)
    if transactions.count() > 0:
        return transactions.first()

def get_transactions_by_user_id(db: Session, user_id: int) -> Transaction:
    transactions = db.query(Transaction).filter(Transaction.nft_owner_id == id)
    if transactions.count() > 0:
        return transactions.first()        

def create_transaction(db: Session, transaction: TransactionCreate) -> None:
    db_object = Transaction(**transaction.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
