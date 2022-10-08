class TaskAssign(Base):
    __tablename__ = "taskassign"
    id = Column(Integer, primary_key=True, index=True)
    done = Column(Type.Boolean,nullable=False)