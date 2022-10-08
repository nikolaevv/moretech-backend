from __future__ import absolute_import
from sqlalchemy.orm import Session
from internal.models.task import Task
from internal.schemas.schemas import TaskCreate


def get_tasks(db: Session) -> list[Task]:
    return db.query(Task).all()

def get_task_by_id(db: Session, id: int) -> Task:
    tasks = db.query(Task).filter(Task.id == id)
    if tasks.count() > 0:
        return tasks.first()

def create_task(db: Session, task: TaskCreate) -> None:
    db_object = Task(**task.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)