from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class HousingTypes(str, Enum):
        house = "house"
        apartment = "apartment"

class Housing(BaseModel):
        areas: float = Field(gt=0, le=2000)
        bedrooms: int = Field(ge=0)
        bathrooms: int = Field(ge=0)
        parkingSpots: int = Field(ge=0)
        type: HousingTypes
        neighborhood: str = Field(min_length=0)

class InputDataDTO(BaseModel):
        housings: List[Housing]
