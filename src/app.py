from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from schemas import PostCreate
from db import Post, create_async_engine, create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload/")
async def upload_file():
    pass

