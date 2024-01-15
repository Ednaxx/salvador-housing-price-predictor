from pydantic import BaseModel

class XGBRequestDTO(BaseModel):
        areas: float | None = None
        bedrooms: int | None = None
        bathrooms: int | None = None
        parkingSpots: int | None = None
        type: str | None = None
        neighborhood: str | None = None