from fastapi import APIRouter
from src.dto.neighborhoodsResponseDTO import neighborhoodsResponseDTO
import pandas as pd

neighborhoods = APIRouter()

@neighborhoods.get("/neighborhoods", tags=["neighborhoods"])
async def get_neighborhoods() -> neighborhoodsResponseDTO:

    df = pd.read_csv("./data/neighborhoods_area_price.csv")
    df = df.fillna(0)
    neighborhoods = df.to_dict(orient='records')

    return { "neighborhoods": neighborhoods }
