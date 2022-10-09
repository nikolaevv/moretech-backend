import datetime

from internal.models.task import User, Transaction
from pkg.db.db import SessionLocal, engine, Base

db = SessionLocal()

Base.metadata.create_all(bind=engine)

db_record = User(
    login = "userr",
    password_hash = "$2a$12$xsgV07dXQO73EmxlHwutZucHbVDVf5NVI6H21POvZ4SD3CytsBGxe",
    token = "user",
    name = "user",
    work_adress = "user",
    gitlab_token = "user",
    public_key = "user",
    private_key = "user",
)

db.add(db_record)

db_record = Transaction(
    ended_at=datetime.datetime.now(),
)

db.add(db_record)

db.commit()
db.close()