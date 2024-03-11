from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Base ready")
    yield
    await delete_tables()
    print("Base clear")


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
