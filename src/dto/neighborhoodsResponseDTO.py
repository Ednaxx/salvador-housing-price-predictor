from pydantic import BaseModel
from typing import List

class neighborhood(BaseModel):
    neighborhood: str
    neighborhood_apartment_area_price: float
    neighborhood_house_area_price: float


class neighborhoodsResponseDTO(BaseModel):
    neighborhoods: List[neighborhood]
