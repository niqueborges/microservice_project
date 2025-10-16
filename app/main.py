from fastapi import FastAPI
from .routers import users
from .database import engine, Base

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Microservice")

app.include_router(users.router)
