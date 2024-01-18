from pydantic import BaseModel
from typing import List

class PredictionResponseDTO(BaseModel):
    predictions: List[float]
