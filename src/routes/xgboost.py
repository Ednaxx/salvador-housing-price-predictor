from fastapi import APIRouter
from src.models.xgb_predict import predict
from src.dto.PredictionRequestDTO import PredictionRequestDTO
from src.dto.PredictionResponseDTO import PredictionResponseDTO
import joblib


xgboost = APIRouter()

@xgboost.post("/predict", tags=["xgboost"])
async def make_prediction(request: PredictionRequestDTO) -> PredictionResponseDTO:
    model = joblib.load("./models/xgb.pkl")
    data = [housing.__dict__ for housing in request.housings]

    predictions = predict(data, model)

    return { "predictions": predictions }
