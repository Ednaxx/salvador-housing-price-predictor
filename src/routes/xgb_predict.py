import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import APIRouter
from src.models.xgb_predict import predict
from src.dto.InputDataDTO import InputDataDTO
import joblib


xgb_predict = APIRouter()

@xgb_predict.post("/", tags=["xgboost"])
async def make_prediction(request: InputDataDTO):
    model = joblib.load("./models/xgb.pkl")

    data = [housing.__dict__ for housing in request.housings]

    return { "prediction": predict(data, model) }
