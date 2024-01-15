import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import APIRouter
from src.models.xgb_predict import predict
from src.dto.XGBRequestDTO import XGBRequestDTO
import joblib


xgb_predict = APIRouter()

@xgb_predict.post("/", tags=["xgboost"])
async def make_prediction(request: XGBRequestDTO):
    model = joblib.load("./models/xgb.pkl")

    data = {
        "areas": request.areas,
        "bedrooms": request.bedrooms,
        "bathrooms": request.bathrooms,
        "parkingSpots": request.parkingSpots,
        "type": request.type,
        "neighborhood": request.neighborhood
    }

    return {"prediction": predict(data, model)}
