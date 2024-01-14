import joblib
import pandas as pd
import numpy as np

def predict(df):
    model = joblib.load("./models/xgb.pkl")

    return model.predict(df)

if __name__ == "__main__":
    # df = pd.DataFrame({
    #     "areas": 60,
    #     "bedrooms": 2,
    #     "bathrooms": 2,
    #     "parkingSpots": 1,
    #     "type": "house",
    #     "neighborhood": "Tororó",
    #     "neighborhood_area_price": np.nan
    # }, index=[123])

    df = pd.DataFrame({
        "areas": 60,
        "bedrooms": 2,
        "bathrooms": 2,
        "parkingSpots": 1,
        "type": "0",
        "neighborhood": "Tororó",
        "neighborhood_area_price": np.nan
    }, index=[123])

    prediction = predict(df)
    print(prediction)
