from fastapi import FastAPI
from src.routes.xgboost import xgboost
from src.routes.neighborhoods import neighborhoods

app = FastAPI(title="Salvador Housing Price Predictor", description="A machine learning API for housing prices prediction in Brazil, Bahia, Salvador.")

app.include_router(xgboost, prefix="/xgboost")
app.include_router(neighborhoods, prefix="/neighborhoods")
