import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
import pandas as pd
from features.build_features import feature__neighborhood_area_price


def predict(df, model):
    df = pd.DataFrame(df)

    neighborhoods_area_price = pd.read_csv("./data/neighborhoods_area_price.csv", index_col="neighborhood")

    feature__neighborhood_area_price(df, neighborhoods_area_price)

    df.type = df.type.replace({"house": 0, "apartment": 1})

    return model.predict(df).tolist()


if __name__ == "__main__":
    model = joblib.load("./models/xgb.pkl")

    df = {
        "areas": 50,
        "bedrooms": 2,
        "bathrooms": 2,
        "parkingSpots": 1,
        "type": "apartment",
        "neighborhood": "Imbuí"
    }

    # 309228.5

    prediction = predict(df, model)
    print("R$ " + str(prediction))
