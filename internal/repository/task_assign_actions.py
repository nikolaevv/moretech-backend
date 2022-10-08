from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import Taskassign
from internal.schemas.schemas import TaskAssignCreate


def get_taskassigns(db: Session) -> list[Taskassign]:
    return db.query(Taskassign).all()

def get_taskassign_by_id(db: Session, id: int) -> Taskassign:
    taskassigns = db.query(Taskassign).filter(Taskassign.id == id)
    if taskassigns.count() > 0:
        return taskassigns.first()

def create_taskassign(db: Session, task_assign: TaskAssignCreate) -> None:
    db_object = Taskassign(**task_assign.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)