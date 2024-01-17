from pydantic import BaseModel
from typing import List

class Housing(BaseModel):
        areas: float | None = None
        bedrooms: int | None = None
        bathrooms: int | None = None
        parkingSpots: int | None = None
        type: str | None = None
        neighborhood: str | None = None

class InputDataDTO(BaseModel):
        housings: List[Housing]
