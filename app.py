from fastapi import FastAPI
from src.routes.xgb_predict import xgb_predict

app = FastAPI(title="Salvador Housing Price Predictor", description="A machine learning API for housing prices prediction in Brazil, Bahia, Salvador.")

app.include_router(xgb_predict, prefix="/v1/xgboost")
