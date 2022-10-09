from fastapi import FastAPI
from internal.handlers.handlers import routes
from fastapi.middleware.cors import CORSMiddleware

from db_create import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
) 

app.include_router(routes)
