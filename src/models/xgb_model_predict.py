import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
import pandas as pd
import numpy as np
from features.build_features import feature__neighborhood_area_price



def predict(df):
    model = joblib.load("./models/xgb.pkl")

    neighborhoods_area_price = pd.read_csv("./data/neighborhoods_area_price.csv", index_col="neighborhood")

    feature__neighborhood_area_price(df, neighborhoods_area_price)

    df.type = df.type.replace({"house": 0, "apartment": 1})

    return model.predict(df)


if __name__ == "__main__":
    df = pd.DataFrame({
        "areas": 50,
        "bedrooms": 2,
        "bathrooms": 2,
        "parkingSpots": 1,
        "type": "apartment",
        "neighborhood": "Imbuí"
    }, index=[0])
    

    prediction = predict(df)
    print("R$ " + str(prediction))
