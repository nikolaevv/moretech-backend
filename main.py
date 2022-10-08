from fastapi import FastAPI
from internal.handlers.handlers import routes #, admin_routes

app = FastAPI()
app.include_router(routes)
# app.include_router(admin_routes)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}