from fastapi import FastAPI
from src.routes.xgboost import xgboost
from src.routes.neighborhoods import neighborhoods
from src.models.xgb_load import load_model, clear_model, model
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()
    yield
    clear_model()

app = FastAPI(
    title="Salvador Housing Price Predictor",
    description="A machine learning API for housing prices prediction in Brazil, Bahia, Salvador.",
    lifespan=lifespan
    )

app.include_router(xgboost, prefix="/xgboost")
app.include_router(neighborhoods, prefix="/neighborhoods")
