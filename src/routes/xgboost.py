from fastapi import APIRouter
from src.models.xgb_predict import predict
from src.models.xgb_load import model
from src.dto.PredictionRequestDTO import PredictionRequestDTO
from src.dto.PredictionResponseDTO import PredictionResponseDTO


xgboost = APIRouter()

@xgboost.post("/predict", tags=["xgboost"])
async def make_prediction(request: PredictionRequestDTO) -> PredictionResponseDTO:
    data = [housing.__dict__ for housing in request.housings]

    predictions = predict(data, model["xgboost"])

    return { "predictions": predictions }
