import numpy as np
import pandas as pd

def feature__neighborhood_area_price(df, neighborhoods_area_price):
    def set_neighborhood_area_price(x):
        if x.type == "house" and x.neighborhood in neighborhoods_area_price.index:
            return neighborhoods_area_price.loc[x.neighborhood]["neighborhood_house_area_price"]
        elif x.type == "apartment" and x.neighborhood in neighborhoods_area_price.index:
            return neighborhoods_area_price.loc[x.neighborhood]["neighborhood_apartment_area_price"]
        else: return np.nan

    df["neighborhood_area_price"] = df.apply(set_neighborhood_area_price, axis=1)

def build_features(df):
    # Missing neighborhood set to NaN
    df.neighborhood = df.neighborhood.apply(lambda x: np.nan if x == "BA" else x)

    # Drop null prices and outliers
    df = df[~(df.prices.isna())]
    df = df[~(df.areas > 200)]
    df = df[~(df.bedrooms > 5)]
    df = df[~(df.bathrooms > 5)]
    df = df[~(df.parkingSpots > 5)]
    df = df[~(df.prices > 1700000)]

    # neighborhood Price/Area

    neighborhood_house_price_sum =  df[df.type == "house"].groupby("neighborhood").prices.sum()
    neighborhood_house_area_sum =  df[df.type == "house"].groupby("neighborhood").areas.sum()

    neighborhood_apartment_price_sum =  df[df.type == "apartment"].groupby("neighborhood").prices.sum()
    neighborhood_apartment_area_sum =  df[df.type == "apartment"].groupby("neighborhood").areas.sum()

    neighborhood_house_area_price = neighborhood_house_price_sum / neighborhood_house_area_sum
    neighborhood_apartment_area_price = neighborhood_apartment_price_sum / neighborhood_apartment_area_sum


    neighborhoods_area_price = pd.DataFrame({
        "neighborhood_apartment_area_price": neighborhood_apartment_area_price,
        "neighborhood_house_area_price": neighborhood_house_area_price
        })

    # Save relationship for use on prediction
    neighborhoods_area_price.to_csv("./data/neighborhoods_area_price.csv")

    feature__neighborhood_area_price(df, neighborhoods_area_price)

    # Encode
    
    df.type = df.type.replace({"house": 0, "apartment": 1})

    return df