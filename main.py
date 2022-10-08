from fastapi import FastAPI
from internal.handlers.handlers import routes

app = FastAPI()
app.include_router(routes)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}