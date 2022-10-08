from __future__ import absolute_import
from sqlalchemy import Column, Table, ForeignKey

from pkg.db.db import Base

user_groups_table = Table(
    "user_groups",
    Base.metadata,
    Column("group_id", ForeignKey("group.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)