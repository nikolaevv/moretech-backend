from fastapi import FastAPI
from pkg.db.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
async def root():
    await get_db()
    return {"message": "Hello Bigger Applications!"}