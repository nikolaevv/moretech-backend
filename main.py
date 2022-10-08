from fastapi import FastAPI
from internal.handlers.handlers import routes #, admin_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
) 

app.include_router(routes)
# app.include_router(admin_routes)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}