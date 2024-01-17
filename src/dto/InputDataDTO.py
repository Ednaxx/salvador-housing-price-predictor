from pydantic import BaseModel
from typing import List
from enum import Enum

class HousingTypes(str, Enum):
        house = "house"
        apartment = "apartment"

class Housing(BaseModel):
        areas: float | None = None
        bedrooms: int | None = None
        bathrooms: int | None = None
        parkingSpots: int | None = None
        type: HousingTypes
        neighborhood: str | None = None

class InputDataDTO(BaseModel):
        housings: List[Housing]
